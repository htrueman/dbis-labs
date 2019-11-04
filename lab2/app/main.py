import csv

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_bootstrap import Bootstrap

from .forms import UserForm, GroupForm, LectureForm, UniversityForm
from .db_models import User, session, Group, Lecture, LectureActivity, University, Subject


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app


app = create_app()


@app.route('/', methods=['get'])
def dashboard():

    return render_template('dashboard.html')


@app.route('/users/', methods=['get', 'post'])
def users():
    if request.method == 'GET':
        form = UserForm()
        return render_template('users.html', form=form, users={u.user_id: u.full_name for u in session.query(User).all()})
    else:
        user = User()
        form = UserForm(request.form)
        if form.validate():
            form.populate_obj(user)
            session.add(user)
            session.commit()
        return render_template(
            'users.html',
            users={u.user_id: u.full_name for u in session.query(User).all()},
            form=form
        )


@app.route('/users/<user_id>/', methods=['get', 'put', 'delete'])
def user(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    form = UserForm(request.form, user)
    template_name = 'user.html'

    if request.method == 'PUT':
        if form.validate():
            form.populate_obj(user)
            session.add(user)
            session.commit()
        else:
            return jsonify(form.errors), 400
    elif request.method == 'DELETE':
        session.delete(user)
        session.commit()

    return render_template(template_name, user=user, form=form)


@app.route('/groups/', methods=['get', 'post'])
def groups():
    if request.method == 'GET':
        form = GroupForm()
        return render_template('groups.html', form=form, groups={g.group_id: g.name for g in session.query(Group).all()})
    else:
        group = Group()
        form = GroupForm(request.form)
        if form.validate():
            form.populate_obj(group)
            session.add(group)
            session.commit()
        return render_template(
            'groups.html',
            groups={g.group_id: g.name for g in session.query(Group).all()},
            form=form
        )


@app.route('/groups/<group_id>/', methods=['get', 'put', 'delete'])
def group(group_id):
    group = session.query(Group).filter_by(group_id=group_id).first()
    form = GroupForm(request.form, group)
    template_name = 'group.html'

    if request.method == 'PUT':
        if form.validate():
            form.populate_obj(group)
            session.add(group)
            session.commit()
        else:
            return jsonify(form.errors), 400
    elif request.method == 'DELETE':
        session.delete(group)
        session.commit()

    return render_template(template_name, group=group, form=form)


@app.route('/lectures/', methods=['get', 'post'])
def lectures():
    if request.method == 'GET':
        form = LectureForm()
        return render_template('lectures.html', form=form, lectures={l.lecture_id: l.version for l in session.query(Lecture).all()})
    else:
        lecture = Lecture()
        form = LectureForm(request.form)
        if form.validate():
            form.populate_obj(lecture)
            session.add(lecture)
            session.commit()
        return render_template(
            'lectures.html',
            lectures={l.lecture_id: l.version for l in session.query(Lecture).all()},
            form=form
        )


@app.route('/lectures/<lecture_id>/', methods=['get', 'put', 'delete'])
def lecture(lecture_id):
    lecture = session.query(Lecture).filter_by(lecture_id=lecture_id).first()
    form = LectureForm(request.form, lecture)
    template_name = 'lecture.html'

    if request.method == 'PUT':
        if form.validate():
            form.populate_obj(lecture)
            session.add(lecture)
            session.commit()
        else:
            return jsonify(form.errors), 400
    elif request.method == 'DELETE':
        session.delete(lecture)
        session.commit()

    return render_template(template_name, lecture=lecture, form=form)


@app.route('/plots/', methods=['get'])
def get_plot_data_file():
    activities = session.query(LectureActivity).all()

    with open('app/static/csv/plot1.csv', mode='w+') as p:
        p_writer = csv.writer(p, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        p_writer.writerow(['activities_count', 'grade'])
        for activity in activities:
            p_writer.writerow([activity.comment_count + activity.view_count + activity.like_count, activity.grade])

    with open('app/static/csv/plot2.csv', mode='w+') as p:
        p_writer = csv.writer(p, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        p_writer.writerow(['student_id', 'grade'])
        for activity in activities:
            user_activities = session.query(LectureActivity).filter_by(student_id=activity.student_id)
            activities_count = 0
            grade_sum = 0
            avg_grade = 0
            for a in user_activities:
                activities_count += 1
                grade_sum += a.grade

            if activities_count > 0:
                avg_grade = grade_sum / activities_count

            p_writer.writerow([activity.student_id, avg_grade])

    return jsonify()


@app.route('/get/', methods=['get'])
def add_test_universities():
    s1 = Subject(
        name='subject1',
        teacher_id=2,
        lecture_id=2
    )
    s2 = Subject(
        name='subject2',
        teacher_id=3,
        lecture_id=3
    )

    u1 = University(
        name='KPI',
        city='Kyiv',
        count_staff=500,
        year=1900
    )
    u2 = University(
        name='KNU',
        city='Kyiv',
        count_staff=1000,
        year=1800
    )
    u3 = University(
        name='LNU',
        city='Lviv',
        count_staff=700,
        year=1901
    )
    u1.subjects.append(s1)
    u1.subjects.append(s2)
    u2.subjects.append(s2)
    u3.subjects.append(s1)

    session.add(u1)
    session.add(u2)
    session.add(u3)
    session.commit()

    return jsonify()


@app.route('/new/', methods=['get'])
def get_test_universities():
    return render_template('new.html', univers=session.query(University).all())


@app.route('/update/', methods=['post', 'get'])
def update_universities():
    university = session.query(University).all()[0]
    form = UniversityForm(request.form, university)

    if request.method == 'POST':
        if form.validate():
            form.populate_obj(university)
            session.add(university)
            session.commit()

    return render_template('update.html', university=university, form=form)

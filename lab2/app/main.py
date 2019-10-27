from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap

from .forms import UserForm, GroupForm, LectureForm
from .db_models import User, session, Group, Lecture


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
        return render_template('groups.html', form=form, groups={g.name: '' for g in session.query(Group).all()})
    else:
        group = Group()
        form = GroupForm(request.form)
        if form.validate():
            form.populate_obj(group)
            session.add(group)
            session.commit()
        return render_template(
            'groups.html',
            groups={g.name: '' for g in session.query(Group).all()},
            form=form
        )


@app.route('/groups/<name>/', methods=['get', 'put', 'delete'])
def group(name):
    group = session.query(Group).filter_by(name=name).first()
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
        group.delete()
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

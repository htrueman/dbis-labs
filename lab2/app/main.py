from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from .forms import UserForm
from .db_models import User, session


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app


app = create_app()


# @app.route('/api/<action>', methods=['GET'])
# def apiGet(action):
#     if action == "number":
#         if 'number' not in session.keys():
#             number = ''
#         else:
#             number = session['number']
#         if not number:
#             number = request.cookies.get('number') if request.cookies.get('number') else ''
#         return render_template("number.html", number=number)
#     else:
#         return render_template("404.html")


@app.route('/', methods=['get'])
def dashboard():

    return render_template('dashboard.html')


@app.route('/users/', methods=['get', 'post'])
def users():
    import pdb
    pdb.set_trace()
    if request.method == 'post':
        form = UserForm()

        return render_template('users.html', form=form)
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

    if request.method == 'put':
        import pdb
        pdb.set_trace()
        if form.validate():
            form.populate_obj(user)
            session.add(user)
            session.commit()
    elif request.method == 'delete':
        user.delete()
        session.commit()

    return render_template(template_name, user=user, form=form)

from flask import Flask, render_template, redirect, url_for
from model import db, Pet, Type
from form import PetForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)
with app.app_context():
    db.create_all()
@app.route('/', methods=['GET', 'POST'])
def index():
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)
        pet_type = Type(name=form.name.data, type=form.type.data)
        db.session.add(pet)
        db.session.add(pet_type)
        db.session.commit()
        return redirect(url_for('index'))
    pet= Pet.query.all()
    pet_type = Type.query.all()
    return render_template('view_pets.html', form=form, pet=pet, pet_type=pet_type)
if __name__ == '__main__':
    app.run(debug=True)
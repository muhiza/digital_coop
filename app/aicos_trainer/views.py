from flask import render_template, flash, url_for, redirect
from flask_login import login_required, current_user
from . import aicos_trainer
from .forms import *
from .. models import *

@aicos_trainer.route('/')
def trainer_dashboard():
    training = Training.query.all()
    training_count = Training.query.count()
    applied_training = applyTraining.query.all()
    applied_training_count = applyTraining.query.count()
    return render_template('trainer_dashboard.html', title="E trainer templates",
                            training_count=training_count,
                            applied_training_count=applied_training_count)


@aicos_trainer.route('/trainingList')
def trainingList():
    applied_training = applyTraining.query.all()
    return render_template('trainingList.html', applied_training=applied_training)


@aicos_trainer.route('/ProvidedtrainingList')
def providedTrainingList():
    provided_training = Training.query.all()
    return render_template('ProvidedTrainingList.html', provided_training=provided_training)





@aicos_trainer.route('/trainer/Apply', methods=['GET', 'POST'])
def applyTrainingzx():
    form = applyTrainingForm()
    if form.validate_on_submit():

        newTraining = applyTraining(
                                namea = form.ingingo.data,
                                abouta = form.abouta.data,
                                descriptiona = form.descriptiona.data,
                                datea       = form.datea.data,
                                department_id = current_user.email
                                )
        try:
            db.session.add(newTraining)
            db.session.commit()
            flash("Umaze gusaba amahugurwa neza!")
        except:
            flash("Ntago amakuru watanze ameze neza!")
        return redirect(url_for('aicos_trainer.trainer_dashboard'))
    return render_template('training.html', form=form)
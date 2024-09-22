from .models import Tbl_Trainer

def trainer(request):
    trainer = Tbl_Trainer.objects.filter(trainer_approval=True,trainer_status=True)
    return {

        'trainer':trainer
    }
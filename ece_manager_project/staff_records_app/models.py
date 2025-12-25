from . import models_folder as _models_folder
from .models_folder.base_activity_model import BaseActivity
from .models_folder.activities_models.journal_publications import JournalPublication
from .models_folder.activities_models.event_attended import EventAttended   
from .models_folder.activities_models.patents import Patent

activity_candidates = [
    "JournalPublication",  
    "EventAttended",
    "AwardAchievement",
    "BookChapter",
    "FundedProjectProposal",
    "GuestPerformance",
    "Patent",
    "ProfessionalMembership",
    "JournalReviewer",
    "InternationalConference",
]

__all__ = [name for name in dir(_models_folder) if not name.startswith("_")]








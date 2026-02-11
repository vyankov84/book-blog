from django.db import models

class BookGenreChoices(models.TextChoices):

    FANTASY = 'FA','FANTASY'
    SCI_FI = 'SCI','SCI_FI'
    ROMANCE = 'RO','ROMANCE'
    MYSTERY = 'MY','MYSTERY'
    THRILLER = 'THR','THRILLER'
    HORROR = 'HO','HORROR'
    HISTORICAL ='HH','HISTORICAL'
    LITERARY = 'LI','LITERARY'
    BIOGRAPHY = 'BG','BIOGRAPHY'
    SCIENCE = 'SC','SCIENCE'
    CRIME = 'CR', 'CRIME'
    OTHER = 'OT','OTHER'


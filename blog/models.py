from django.db import models

# Create a blog model.
    # title
    # pub_date
    # body
    # images

# Add blog app to the settings

#create a migrration

# Migrate

# Add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    images = models.ImageField(upload_to='images/')

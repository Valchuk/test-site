from django.db import models

class Article(models.Model):
    
    class Meta:
        db_table = 'article'
        
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField('date published')
    article_likes = models.IntegerField(default=0)
    
    def _str_(self):
        return smart_text(self.article_tittle)

    
class Comment(models.Model):
    class Meta():
        db_table = 'comment'
        
    comment_text = models.TextField()
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)

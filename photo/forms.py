from django.forms import ModelForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    '''ModedlFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields:フォームで使用するフィールドを指定
        '''
        
        model = PhotoPost
        fields = ('category', 'title', 'comment', 'image1', 'image2')
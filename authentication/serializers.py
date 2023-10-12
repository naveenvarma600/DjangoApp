import shutil
from numpy import require
from rest_framework import serializers
from .models import *


class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Files
        fields = '__all__'

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000 , allow_empty_file = False , use_url = False)
    )
    # viewonceonly = serializers.
    folder = serializers.CharField(required = False)
    viewonceonly = serializers.BooleanField(required=False) 
    
    def zip_files(self,folder):
        shutil.make_archive(f'static/zip/{folder}' , 'zip' ,f'static/{folder}' )

    def create(self , validated_data):
        folder = Folder.objects.create()
        if validated_data.pop('viewonceonly') == True:
            print("marking it as true")
            folder.viewonce = True
            print("marked true")
            folder.save()
        else:
            print("marke as false")
        print("whole data issss",*validated_data)
        print("just checking",validated_data['files'])
        files = validated_data.pop('files')
        print("checking here")
        print("finally, checked is ")
        # print("chekc d i s",validated_data.pop('viewonceonly'))
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder = folder , file = file) 
            files_objs.append(files_obj)
        print("working till appending")
        # print("validated data is ",validated_data.pop('files'))
        # print("from serialzers",validated_data.pop('viewonceonly'))
        self.zip_files(folder.uid)
        print("zipping is donee,maybe problem in returning")

        return {'files' : {} , 'folder' : str(folder.uid)}
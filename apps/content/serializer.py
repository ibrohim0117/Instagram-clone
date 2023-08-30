from collections import OrderedDict

from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, ListField, SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import ModelSerializer

from content.models import file_ext_validator, Post, Media


class PostModelSerializer(ModelSerializer):
    id = CharField(read_only=True)
    media = ListField(validators=(file_ext_validator, ))

    class Meta:
        model = Post
        fields = ['__all__']
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comments', 'id')

    def create(self, validated_data):
        medias = validated_data.pop('media', [])
        media_ids = []
        if len(medias) > 10:
            raise ValidationError('10 tadan kup narsa joylab bulmaydi')
        for media in medias:
            file = Media.objects.create(file=media)
            media_ids.append(file.id)
        validated_data['media'] = media_ids
        return super().create(validated_data)

    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            elif hasattr(attribute, 'all'):
                ret[field.field_name] = [field.file.url for field in attribute.all()]
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret


class UpdatePostModelSerializer(ModelSerializer):
    model = Post
    fields = ['caption', 'location']
    read_only_fields = ('created_at', 'updated_at', 'likes', 'comments', 'id')

    def to_representation(self, instance):
        return super().to_representation(instance)









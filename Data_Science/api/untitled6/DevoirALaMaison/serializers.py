from rest_framework import serializers
from DevoirALaMaison.models import Subject

class SubjectSerializer(serializers.Serializer) :
    IDSubject = serializers.IntegerField()
    AGE = serializers.IntegerField()
    SPORT = serializers.IntegerField()
    label = serializers.FloatField()
    xchest = serializers.FloatField()
    ychest = serializers.FloatField()
    zchest = serializers.FloatField()
    ecg = serializers.FloatField()
    resp = serializers.FloatField()
    xwrist = serializers.FloatField()
    ywrist = serializers.FloatField()
    zwrist = serializers.FloatField()
    bvp = serializers.FloatField()
    temp = serializers.FloatField()
    activity = serializers.FloatField(allow_null=True)

    def create (self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.IDSubject = validated_data.get('IDSubject',instance.IDSubject)
        instance.AGE = validated_data.get('AGE',instance.AGE)
        instance.SPORT = validated_data.get('SPORT',instance.SPORT)
        instance.label = validated_data.get('label',instance.label)
        instance.xchest = validated_data.get('xchest',instance.xchest)
        instance.ychest = validated_data.get('ychest',instance.ychest)
        instance.zchest = validated_data.get('zchest',instance.zchest)
        instance.ecg = validated_data.get('ecg',instance.ecg)
        instance.resp = validated_data.get('resp',instance.resp)
        instance.xwrist = validated_data.get('xwrist',instance.xwrist)
        instance.ywrist = validated_data.get('ywrist',instance.ywrist)
        instance.zwrist = validated_data.get('zwrist',instance.zwrist)
        instance.bvp = validated_data.get('bvp',instance.bvp)
        instance.temp = validated_data.get('temp',instance.temp)

        instance.save()
        return instance
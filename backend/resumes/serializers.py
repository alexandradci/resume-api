from rest_framework import serializers
from .models import Resume, Skill, JobHistory, EducationHistory
from django.db import transaction

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'skill_level')


class JobHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = ('id', 'start_date', 'end_date', 'job_title', 'description')


class EducationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistory
        fields = ('id', 'name', 'qualification')


class ResumeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    skills = SkillSerializer(many=True, required=False)
    job_history = JobHistorySerializer(many=True, required=False)
    education_history = EducationHistorySerializer(many=True, required=False)

    class Meta:
        model = Resume
        fields = (
            'id', 'owner', 'name', 'bio', 'address',
            'job_history', 'skills', 'education_history', 'created_at',
        )

    def create(self, validated_data):
        skills_data = validated_data.pop('skills', [])
        job_history_data = validated_data.pop('job_history', [])
        education_history_data = validated_data.pop('education_history', [])

        resume = Resume.objects.create(**validated_data)

        for skill in skills_data:
            Skill.objects.create(resume=resume, **skill)
        for job in job_history_data:
            JobHistory.objects.create(resume=resume, **job)
        for edu in education_history_data:
            EducationHistory.objects.create(resume=resume, **edu)

        return resume

def update(self, instance, validated_data):
    skills_data = validated_data.pop('skills', [])
    job_history_data = validated_data.pop('job_history', [])
    education_history_data = validated_data.pop('education_history', [])

    with transaction.atomic(): 
        instance.name = validated_data.get('name', instance.name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        # Clear and recreate nested data
        instance.skills.all().delete()
        instance.job_history.all().delete()
        instance.education_history.all().delete()

        for skill in skills_data:
            Skill.objects.create(resume=instance, **skill)
        for job in job_history_data:
            JobHistory.objects.create(resume=instance, **job)
        for edu in education_history_data:
            EducationHistory.objects.create(resume=instance, **edu)

    return instance


        

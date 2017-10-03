from .models import InstitutionType, ParticipantInstitution, ContactType
from .models import Switch
from .models import Contact
from rest_framework import serializers


class ParticipantInstitutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionType
        fields = [
            'id',
            'description',
        ]


class ParticipantInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantInstitution
        institution_type = ParticipantInstitutionTypeSerializer(many=True,
                                                                read_only=True)
        fields = [
            'id',
            'name',
            'institution_type',
        ]


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactType
        fields = ['id', 'description']


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        contact_type = ContactTypeSerializer(many=True, read_only=True)
        ipa_code = ParticipantInstitutionSerializer()
        fields = [
                    'id',
                    'name',
                    'phone_number',
                    'email',
                    'priority',
                    'contact_type',
                    'ipa_code',
                ]


class SwitchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Switch
        fields = [
                'serial_number',
                'fabricant',
                'qtd_slots',
                'patrimony_number',
                'site_type',
        ]

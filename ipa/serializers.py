from sigi_op.serializers import SiteSerializer
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import InstitutionType, ParticipantInstitution
from .models import ContactType, Generator
from .models import NoBreak
from .models import Switch
from .models import Slot
from .models import SlotPort
from .models import Contact


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
            'cnpj',
            'sigla',
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


class GeneratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Generator
        site = SiteSerializer(many=True, read_only=True)
        fields = [
            'id',
            'power',
            'manufacturer',
            'patrimony',
            'site',
        ]


class NoBreakSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoBreak
        fields = [
            'id',
            'power',
            'proprietary',
            'patrimony_number',
            'site_id',
        ]


class SwitchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Switch
        fields = [
            'id',
            'serial_number',
            'manufacturer',
            'slots_quantity',
            'patrimony_number',
            'site_id',
        ]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission

        fields = [
            'id',
            'name',
            'content_type',
            'codename',
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        permissions = PermissionSerializer(many=True, read_only=True)
        fields = [
            'id',
            'name',
            'permissions',
        ]


class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        switch_id = SwitchSerializer(read_only=True)
        fields = [
            'id',
            'serie',
            'number',
            'patrimony',
            'band',
            'slot_port_quantity',
            'switch_id',
        ]


class SlotPortSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlotPort
        slot_id = SlotSerializer(read_only=True)
        fields = [
            'id',
            'port_type',
            'port',
            'slot_id',
        ]

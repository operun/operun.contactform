# -*- coding: utf-8 -*-

from operun.contactform import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IControlPanel(Interface):

    send_confirmation = schema.Bool(
        title=_(
            u'controlpanel_contactform_send_confirmation',
            default='Send Confirmation E-Mail',
        ),
        description=_(
            u'controlpanel_contactform_send_confirmation_description',
            default=(u'When enabled, the contact form will send a confirmation to the contact form user.'),  # noqa: 501
        ),
        required=False,
        default=True,
    )


class ControlPanelEditForm(RegistryEditForm):
    schema = IControlPanel
    schema_prefix = 'operun.contactform'
    label = _(u'operun_contactform_title', default=u'operun Contactform')


ControlPanelView = layout.wrap_form(
    ControlPanelEditForm,
    ControlPanelFormWrapper,
)

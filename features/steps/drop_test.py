from behave import *
from trpz_drop import Request
import os


content = Request()


@given(u'file name is "text.txt"')
def step_impl(context):
    assert os.path.isfile('./files/text.txt') is True


@when(u'uploading "text.txt" file to Dropbox')
def step_impl(context):
    content.upload()


@then(u'file "text.txt" is uploaded')
def step_impl(context):
    assert content.response.status_code == 200


@given(u'file named "text.txt" is uploaded')
def step_impl(context):
    assert content.response.status_code == 200


@when(u'requesting metadata of "text.txt" by its id')
def step_impl(context):
    content.get_file(content.id)


@then(u'i receive metadata for "text.txt"')
def step_impl(context):
    assert content.response.status_code == 200


@given(u'i have file path of "text.txt"')
def step_impl(context):
    assert content.file_path is not None


@when(u'i request to delete "text.txt"')
def step_impl(context):
    content.delete_file(content.file_path)


@then(u'file "text.txt" deleted')
def step_impl(context):
    assert content.response.status_code == 200
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, URL, IPAddress, Optional


class DownloadAddress(FlaskForm):
    address = StringField("Please enter the address of the file to be downloaded:",
                          validators=[DataRequired(), URL()])
    submit = SubmitField("Submit")


class CmdText(FlaskForm):
    cmd = StringField("Command:", validators=[DataRequired()])
    submit = SubmitField("Submit")


class Histroy(FlaskForm):
    ip_address = StringField("ip地址", validators=[Optional(), IPAddress()], default=None)
    begin_time = DateTimeField("开始日期", default=None, validators=[Optional()])
    end_time = DateTimeField("结束日期", default=None, validators=[Optional()])
    ret_code = StringField("返回码", default=None, validators=[Optional()])
    submit = SubmitField("查询", default=None)

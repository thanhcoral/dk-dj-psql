from rest_framework.exceptions import APIException
from common import validators


class UrlIsInvalidOrExpired(APIException):
    status_code = 400
    default_detail = "フィールドフォーマットエラー"
    default_code = "UrlIsInvalidOrExpired"


class RefreshTokenFail(APIException):
    status_code = 406
    default_detail = validators.TOKEN_INVALID_OR_EXPIRED_MESSAGE
    default_code = "RefreshTokenFail"


class TokenIsInvalidOrExpired(APIException):
    status_code = 401
    default_detail = validators.TOKEN_INVALID_OR_EXPIRED_MESSAGE
    default_code = "TokenIsInvalidOrExpired"


class TokenIsWrong(APIException):
    status_code = 401
    default_detail = validators.WRONG_TOKEN_MESSAGE
    default_code = "TokenIsInvalidOrExpired"

class TokenIsRequired(APIException):
    status_code = 401
    default_detail = validators.REQUIRED_TOKEN_MESSAGE
    default_code = "TokenIsRequired"


class TokenIsEmpty(APIException):
    status_code = 401
    default_detail = validators.EMPTY_TOKEN
    default_code = "TokenIsEmpty"

    
class ResetPasswordURLIsInvalidOrExpired(APIException):
    status_code = 400
    default_detail = "このURLのパスワード再発行URLは無効です。再度、メールアドレス確認からやり直してください。"
    default_code = "ResetPasswordURLIsInvalidOrExpired"

class NoServicePermission(APIException):
    status_code = 403
    default_detail = validators.NO_SERVICE_PERMISSION_MESSAGE
    default_code = "NoServicePermission"

class FirstLoginExecption(APIException):
    status_code = 400
    default_detail = ""
    default_code = "FirstLoginExecption"

class NoLoginPermission(APIException):
    status_code = 400
    default_detail = validators.NO_SERVICE_PERMISSION_MESSAGE
    default_code = "NoLoginPermission"

class InvalidFormatFieldError(APIException):
    status_code = 400
    default_detail = "メールアドレス形式で入力してください。"
    default_code = "InvalidFormatFieldError"

class ResetPasswordInvalidFormatFieldError(APIException):
    status_code = 400
    default_code = "ResetPasswordInvalidFormatFieldError"

class EmptyEmailPasswordError(APIException):
    status_code = 400
    default_detail = "メールアドレスまたはログインパスワードが未入力です。"
    default_code = "EmptyEmailPasswordError"

class ExistSpaceInEmailPasswordError(APIException):
    status_code = 400
    default_detail = "入力内容が適切ではありません。"
    default_code = "ExistSpaceInEmailPasswordError"


class InvalidEmployeeNumber(APIException):
    status_code = 400
    default_detail = "InvalidEmployeeNumber"
    default_code = "InvalidEmployeeNumber"


class IncorrectCredential(APIException):
    status_code = 400
    default_detail = "ユーザー名、または、パスワードに誤りがあります。"
    default_code = "IncorrectCredential"


class NotExistEmployee(APIException):
    status_code = 400
    default_detail = validators.NOT_FOUND_EMPLOYEE_MESSAGE
    default_code = "NotExistEmployee"

class NotNoticeUnpublic(APIException):
    status_code = 400
    default_detail = "お知らせ情報が公開されていません。"
    default_code = "NotNoticeUnpublic"
    
class PlanExprird(APIException):
    status_code = 403
    default_detail = "お知らせ情報がアクセス権限を持っていません。"
    default_code = "PlanExprird"

class PlanExprirdRequest(APIException):
    status_code = 403
    default_detail = "申請情報がアクセス権限を持っていません。"
    default_code = "PlanExprirdRequest"
class EventEntryExprird(APIException):
    status_code = 403
    default_detail = "お知らせ情報がアクセス権限を持っていません。"
    default_code = "EventEntryExprird"
    
class EventEntryExprirdError(APIException):
    status_code = 400
    default_detail = "イベントに既にエントリーしました。"
    default_code = "EventEntryExprirdError"
    
class EmployeeIsRemoved(APIException):
    status_code = 400
    default_detail = validators.EMPLOYEE_IS_REMOVED_MESSAGE
    default_code = "EmployeeIsRemoved"

class CanNotRemoveOwner(APIException):
    status_code = 400
    default_detail = validators.REMOVE_OWNER_MESSAGE
    default_code = "CanNotRemoveOwner"


class NotExistCompany(APIException):
    status_code = 404
    default_detail = validators.NOT_FOUND_COMPANY_MESSAGE
    default_code = "NotExistCompany"
 
    
class NotExistRequest(APIException):
    status_code = 403
    default_detail = "申請情報がアクセス権限を持っていません。"
    default_code = "NotExistRequest"
    
    
class NotExistEventEntry(APIException):
    status_code = 404
    default_detail = "NotExistEventEntry"
    default_code = "NotExistEventEntry"


class InvalidFileUpload(APIException):
    status_code = 400
    default_detail = "InvalidFileUpload"
    default_code = "InvalidFileUpload"


class InvalidFileTemplate(APIException):
    status_code = 400
    default_detail = "InvalidFileTemplate"
    default_code = "InvalidFileTemplate"


class ExistEmail(APIException):
    status_code = 400
    default_detail = validators.EXIST_EMAIL_MESSAGE
    default_code = "ExistEmail"
    
class InvalidEmail(APIException):
    status_code = 400
    default_detail = "サービスにユーザが存在していません。"
    default_code = "ExistEmail"

class ErrorPermissionEmail(APIException):
    status_code = 400
    default_detail = "オーナーのユーザーのメールアドレスでサービス利用申請ができません。"
    default_code = "ExistEmail"
class ErrorRoleDuplicate(APIException):
    status_code = 400
    default_detail = "既にサービス上で該当の権限が設定済です。"
    default_code = "ExistEmail"


class InternalError(APIException):
    status_code = 500
    default_detail = "システムエラー。"
    default_code = "InternalError"


class CanNotDowngradeUser(APIException):
    status_code = 400
    default_detail = validators.CAN_NOT_DOWNGRADE_USER_MESSAGE
    default_code = "CanNotDowngradeUser"
class RequestAprove(APIException):
    status_code = 400
    default_detail = "申請は既に承認されました。"
    default_code = "RequestAprove"
class RequestDeny(APIException):
    status_code = 400
    default_detail = "申請は既に却下されました。"
    default_code = "RequestDeny"

class RequestDeleteStatus(APIException):
    status_code = 400
    default_detail = "申請情報が削除されました。"
    default_code = "RequestDeleteStatus"
    
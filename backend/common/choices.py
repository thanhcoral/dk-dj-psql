from django.db import models
from django.utils.translation import gettext_lazy as _


class StaffNumber(models.IntegerChoices):
    ZERO = 0, _("1~10人")
    ONE = 1, _("11~50人")
    TWO = 2, _("51~100人")
    THREE = 3, _("101~200人")
    FOUR = 4, _("201~500人")
    FIVE = 5, _("501~1000人")
    SIX = 6, _("1000人以上")


class ContractPlan(models.IntegerChoices):
    # 期限切れ（トライアルor有料プラン期限切れ後、設定のみ利用可能）
    EXPIRED = 0
    # 有料プラン（契約後に全機能利用可能）
    PAID = 1
    # 無料トライアルプラン（無料のお試しで全機能利用可能）
    TRIAL = 2


class PaymentMethod(models.IntegerChoices):
    # 請求書払い
    BILL = 0
    # クレジットカード払い
    CREDIT_CARD = 1


class UserStatus(models.IntegerChoices):
    # 対象外（ログイン権限を持たない一般ユーザ）
    NOT_APPLY = 0
    # 仮登録（初回ログイン設定が完了していない、管理者orオーナーのユーザ）
    TEMPORARY_REGISTRATION = 1
    # 登録済（サービスへのログイン可ユーザー）
    REGISTERED = 2
    # 停止（アカウント停止となったユーザ）
    SUSPENDED = 9


class UserRole(models.IntegerChoices):
    STAFF = 0, _("STAFF (EVERY ONE)")
    DIRECTOR = 1, _("DIRECTOR")
    MANAGER = 2, _("MANAGER")
    OWNER = 3, _("OWNER")


class NoticeStatus(models.IntegerChoices):
    UNPUBLISHED = 0
    PUBLISHED = 1
    STOP_PUBLISHED = 2


class PublishStatusRequest(models.IntegerChoices):
    UNPUBLISH = 1
    PUBLISHED = 2
    STOP_PUBLISH = 3


class ApprovedStatusRequest(models.IntegerChoices):
    IMAPPROVED = 0
    APPROVED = 1
    DENY = 2


class DeleteFlagRequest(models.IntegerChoices):
    VALID_DATA = 0
    REASONABLE_DELETION = 1


class StatusEvent(models.IntegerChoices):
    UNPUBLISHED = 0
    PUBLISHED = 1
    STOP_PUBLISHED = 2


class StatusEventEntry(models.IntegerChoices):
    COMPLETED = 1
    STOP = 2
    CANCEL = 3

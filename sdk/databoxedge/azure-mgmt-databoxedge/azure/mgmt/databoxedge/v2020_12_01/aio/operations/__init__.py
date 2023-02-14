# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._available_skus_operations import AvailableSkusOperations
from ._devices_operations import DevicesOperations
from ._alerts_operations import AlertsOperations
from ._bandwidth_schedules_operations import BandwidthSchedulesOperations
from ._jobs_operations import JobsOperations
from ._nodes_operations import NodesOperations
from ._operations_status_operations import OperationsStatusOperations
from ._orders_operations import OrdersOperations
from ._roles_operations import RolesOperations
from ._addons_operations import AddonsOperations
from ._monitoring_config_operations import MonitoringConfigOperations
from ._shares_operations import SharesOperations
from ._storage_account_credentials_operations import StorageAccountCredentialsOperations
from ._storage_accounts_operations import StorageAccountsOperations
from ._containers_operations import ContainersOperations
from ._triggers_operations import TriggersOperations
from ._users_operations import UsersOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "AvailableSkusOperations",
    "DevicesOperations",
    "AlertsOperations",
    "BandwidthSchedulesOperations",
    "JobsOperations",
    "NodesOperations",
    "OperationsStatusOperations",
    "OrdersOperations",
    "RolesOperations",
    "AddonsOperations",
    "MonitoringConfigOperations",
    "SharesOperations",
    "StorageAccountCredentialsOperations",
    "StorageAccountsOperations",
    "ContainersOperations",
    "TriggersOperations",
    "UsersOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()

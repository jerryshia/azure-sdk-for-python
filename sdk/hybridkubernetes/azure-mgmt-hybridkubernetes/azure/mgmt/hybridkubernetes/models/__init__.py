# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import ConnectedCluster
    from ._models_py3 import ConnectedClusterAADProfile
    from ._models_py3 import ConnectedClusterIdentity
    from ._models_py3 import ConnectedClusterPatch
    from ._models_py3 import CredentialResult
    from ._models_py3 import CredentialResults
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AzureEntityResource
    from ._models import ConnectedCluster
    from ._models import ConnectedClusterAADProfile
    from ._models import ConnectedClusterIdentity
    from ._models import ConnectedClusterPatch
    from ._models import CredentialResult
    from ._models import CredentialResults
    from ._models import ErrorDetails
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import ProxyResource
    from ._models import Resource
    from ._models import TrackedResource
from ._paged_models import ConnectedClusterPaged
from ._paged_models import OperationPaged
from ._connected_kubernetes_client_enums import (
    ResourceIdentityType,
    ProvisioningState,
)

__all__ = [
    'AzureEntityResource',
    'ConnectedCluster',
    'ConnectedClusterAADProfile',
    'ConnectedClusterIdentity',
    'ConnectedClusterPatch',
    'CredentialResult',
    'CredentialResults',
    'ErrorDetails',
    'ErrorResponse', 'ErrorResponseException',
    'Operation',
    'OperationDisplay',
    'ProxyResource',
    'Resource',
    'TrackedResource',
    'ConnectedClusterPaged',
    'OperationPaged',
    'ResourceIdentityType',
    'ProvisioningState',
]

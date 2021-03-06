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

from .auto_scaling_mechanism import AutoScalingMechanism


class AddRemoveReplicaScalingMechanism(AutoScalingMechanism):
    """Describes the horizontal auto scaling mechanism that adds or removes
    replicas (containers or container groups).

    :param kind: Constant filled by server.
    :type kind: str
    :param min_count: Minimum number of containers (scale down won't be
     performed below this number).
    :type min_count: int
    :param max_count: Maximum number of containers (scale up won't be
     performed above this number).
    :type max_count: int
    :param scale_increment: Each time auto scaling is performed, this number
     of containers will be added or removed.
    :type scale_increment: int
    """

    _validation = {
        'kind': {'required': True},
        'min_count': {'required': True},
        'max_count': {'required': True},
        'scale_increment': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'min_count': {'key': 'minCount', 'type': 'int'},
        'max_count': {'key': 'maxCount', 'type': 'int'},
        'scale_increment': {'key': 'scaleIncrement', 'type': 'int'},
    }

    def __init__(self, min_count, max_count, scale_increment):
        super(AddRemoveReplicaScalingMechanism, self).__init__()
        self.min_count = min_count
        self.max_count = max_count
        self.scale_increment = scale_increment
        self.kind = 'AddRemoveReplica'

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

from msrest.serialization import Model


class MongoDbMigrationSettings(Model):
    """Describes how a MongoDB data migration should be performed.

    All required parameters must be populated in order to send to Azure.

    :param boost_rus: The RU limit on a CosmosDB target that collections will
     be temporarily increased to (if lower) during the initial copy of a
     migration, from 10,000 to 1,000,000, or 0 to use the default boost (which
     is generally the maximum), or null to not boost the RUs. This setting has
     no effect on non-CosmosDB targets.
    :type boost_rus: int
    :param databases: Required. The databases on the source cluster to migrate
     to the target. The keys are the names of the databases.
    :type databases: dict[str,
     ~azure.mgmt.datamigration.models.MongoDbDatabaseSettings]
    :param replication: Describes how changes will be replicated from the
     source to the target. The default is OneTime. Possible values include:
     'Disabled', 'OneTime', 'Continuous'
    :type replication: str or
     ~azure.mgmt.datamigration.models.MongoDbReplication
    :param source: Required. Settings used to connect to the source cluster
    :type source: ~azure.mgmt.datamigration.models.MongoDbConnectionInfo
    :param target: Required. Settings used to connect to the target cluster
    :type target: ~azure.mgmt.datamigration.models.MongoDbConnectionInfo
    :param throttling: Settings used to limit the resource usage of the
     migration
    :type throttling:
     ~azure.mgmt.datamigration.models.MongoDbThrottlingSettings
    """

    _validation = {
        'databases': {'required': True},
        'source': {'required': True},
        'target': {'required': True},
    }

    _attribute_map = {
        'boost_rus': {'key': 'boostRUs', 'type': 'int'},
        'databases': {'key': 'databases', 'type': '{MongoDbDatabaseSettings}'},
        'replication': {'key': 'replication', 'type': 'str'},
        'source': {'key': 'source', 'type': 'MongoDbConnectionInfo'},
        'target': {'key': 'target', 'type': 'MongoDbConnectionInfo'},
        'throttling': {'key': 'throttling', 'type': 'MongoDbThrottlingSettings'},
    }

    def __init__(self, *, databases, source, target, boost_rus: int=None, replication=None, throttling=None, **kwargs) -> None:
        super(MongoDbMigrationSettings, self).__init__(**kwargs)
        self.boost_rus = boost_rus
        self.databases = databases
        self.replication = replication
        self.source = source
        self.target = target
        self.throttling = throttling

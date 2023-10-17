from dbt.adapters.proton.connections import ProtonConnectionManager  # noqa
from dbt.adapters.proton.connections import ProtonCredentials
from dbt.adapters.proton.relation import ProtonRelation  # noqa
from dbt.adapters.proton.column import ProtonColumn  # noqa
from dbt.adapters.proton.impl import ProtonAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import proton


Plugin = AdapterPlugin(
    adapter=ProtonAdapter,
    credentials=ProtonCredentials,
    include_path=proton.PACKAGE_PATH)

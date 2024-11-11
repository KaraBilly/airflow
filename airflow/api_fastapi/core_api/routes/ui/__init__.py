# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from airflow.api_fastapi.common.router import AirflowRouter
from airflow.api_fastapi.core_api.routes.ui.assets import assets_router
from airflow.api_fastapi.core_api.routes.ui.dags import dags_router
from airflow.api_fastapi.core_api.routes.ui.dashboard import dashboard_router

ui_router = AirflowRouter(prefix="/ui")

ui_router.include_router(assets_router)
ui_router.include_router(dashboard_router)
ui_router.include_router(dags_router)
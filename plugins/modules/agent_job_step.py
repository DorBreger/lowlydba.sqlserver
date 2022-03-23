#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2022, John McCall (@lowlydba)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: agent_job_step
short_description: Configures a SQL Agent job step.
description:
  - Configures a step for an agent job.
options:
  job:
    description:
      - The name of the job to which to add the step.
    required: true
    type: str
  step_id:
    description:
      - The sequence identification number for the job step. Step identification numbers start at 1 and increment without gaps.
        Required if state is C(present).
    required: false
    type: int
  step_name:
    description:
      - The name of the step.
    required: true
    type: str
  database:
    description:
      - The name of the database in which to execute a Transact-SQL step. The default is 'master'.
    required: false
    type: str
    default: 'master'
  subsystem:
    description:
      - The subsystem used by the SQL Server Agent service to execute command.
    required: false
    type: str
    default: 'TransactSql'
    choices: ['CmdExec', 'Distribution', 'LogReader', 'Merge', 'PowerShell', 'QueueReader', 'Snapshot', 'Ssis', 'TransactSql']
  command:
    description:
      - The commands to be executed by SQLServerAgent service through subsystem.
    required: false
    type: str
  on_success_action:
    description:
      - The action to perform if the step succeeds.
    required: false
    type: str
    default: 'QuitWithSuccess'
    choices: ['QuitWithSuccess', 'QuitWithFailure', 'GoToNextStep', 'GoToStep']
  on_success_step_id:
    description:
      - The ID of the step in this job to execute if the step succeeds and OnSuccessAction is 'GoToStep'.
    required: false
    type: int
    default: 0
  on_fail_action:
    description:
      - The action to perform if the step fails.
    required: false
    type: str
    default: 'QuitWithFailure'
    choices: ['QuitWithSuccess', 'QuitWithFailure', 'GoToNextStep', 'GoToStep']
  on_fail_step_id:
    description:
      - The ID of the step in this job to execute if the step fails and OnFailAction is "GoToStep".
    required: false
    type: int
    default: 0
  retry_attempts:
    description:
      - The number of retry attempts to use if this step fails. The default is 0.
    required: false
    type: int
    default: 0
  retry_interval:
    description:
      - The amount of time in minutes between retry attempts.
    required: false
    type: int
    default: 0
  state:
    description:
      - Whether or not the job step should be C(present) or C(absent).
    required: false
    type: str
    default: 'present'
    choices: ['present', 'absent']
author: "John McCall (@lowlydba)"
notes:
  - Check mode is supported.
extends_documentation_fragment:
  - lowlydba.sqlserver.sql_credentials
'''

EXAMPLES = r'''
- name: Create a job step
  lowlydba.sqlserver.agent_job_step:
'''

RETURN = r'''
data:
  description: Output from the C(New-DbaAgentJobStep), C(Set-DbaAgentJobStep), or C(Remove-DbaAgentJobStep) function.
  returned: success
  type: dict
'''
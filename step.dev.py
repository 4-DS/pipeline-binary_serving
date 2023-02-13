from sinara.step import Step
from sinara.step import StepSafeguard as sg

try:
    step = Step(run_params_file_globs="params/step_params.json",
           env_name="user")
    for notebook in step.notebooks:
        notebook.run()
except Exception as e:
    step.handle_exception(e)
finally:
    step.handle_exit()

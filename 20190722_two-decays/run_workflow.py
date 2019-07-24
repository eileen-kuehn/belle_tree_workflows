#!/usr/local/bin/python

import os
import json
import click
import logging

from assess_workflows.generic.workflow import Workflow
from assess_workflows.generic.structure import Structure


@click.command()
@click.option("--start", "start", required=False, default=0)
@click.option("--end", "end", required=False, type=int)
def start(start, end):
    env_vars = json.load(open(os.path.join(os.path.dirname(__file__), os.pardir, "base_configuration.json"), "r"))
    env_vars.update(json.load(open(os.path.join(os.path.dirname(__file__), "workflow_configuration.json"), "r")))
    if env_vars["DISS_BASEPATH"].startswith("./") or env_vars["DISS_BASEPATH"] == ".":
        env_vars["DISS_BASEPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, env_vars["DISS_BASEPATH"][1:]))
    if env_vars["DISS_BASEPATH"] == "..":
        env_vars["DISS_BASEPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, env_vars["DISS_BASEPATH"][2:]))
    if env_vars["DISS_WORKFLOWFOLDER_NAME"] == ".":
        env_vars["DISS_WORKFLOWFOLDER_NAME"] = os.path.basename(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    workflow = Workflow()
    workflow.add_task(
        cli_path=Structure.data_selection_cli(),
        cmd="index-valid-hdf-trees",
        save=True,
        pcount=1,
        paths=[
            os.path.join(os.path.dirname(__file__), os.pardir, "data/trees/Bd_Kpi_mdst_000001_prod00006875_task00000001.h5"),
            os.path.join(os.path.dirname(__file__), os.pardir, "data/trees/Bd_Kspi0_mdst_000001_prod00006201_task00000001.h5")
        ],
        name="Index valid HDF trees"
    )
    workflow.prepare_intermediate_as_input(reference="Index valid HDF trees")
    workflow.add_task(
        cli_path=Structure.workflow_cli(),
        cmd="process-as-matrix",
        save=True,
        hdf=True,
        use_input=True,
        name="Generate Distance Matrix",
        pcount=2
    )
    # finalise results
    workflow.finalise(file_type="h5", reference="Generate Distance Matrix")
    workflow.execute(env_vars, start=start, end=end)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.WARNING)
    logging.getLogger('EXCEPTION').setLevel(logging.INFO)
    start()

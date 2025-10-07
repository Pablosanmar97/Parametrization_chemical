import yaml
import os
import itertools

# Base template
base_yaml = {
    "HR1": {
        "e": 3.281,
        "mu": 0.0029,
        "S": 4,
        "a": 1,
        "b": 3,
        "c": 1,
        "d": 5,
        "xr": -1.6,
        "vh": 1
    },
    "HR2": {
        "e": 3.281,
        "mu": 0.0039,
        "S": 4,
        "a": 1,
        "b": 3,
        "c": 1,
        "d": 5,
        "xr": -1.6,
        "vh": 1
    },
    "Chemical-HR1-HR2": {
        "gfast": 0.015,
        "Esyn": -1.5,
        "sfast": 0.2,
        "Vfast": -0,
        "Vslow": -0,
        "gslow": 0 ,
        "k1": 1,
        "k2": 0.03,
        "sslow": 1
    },
    "Chemical-HR2-HR1": {
        "gfast": 0.015,
        "Esyn": -1.5,
        "sfast": 0.2,
        "Vfast": -0,
        "Vslow": -0,
        "gslow": 0.025,
        "k1": 1,
        "k2": 0.03,
        "sslow": 1
    }
}

def generate_yaml(filename, VpreVpos_params):
    yaml_data = base_yaml.copy()
    yaml_data["Chemical-HR1-HR2"].update(VpreVpos_params)
    
    with open(filename, "w") as f:
        yaml.dump(yaml_data, f, sort_keys=False)
    print(f"Saved: {filename}")

if __name__ == "__main__":
    output_dir = "yaml_configs"
    os.makedirs(output_dir, exist_ok=True)

    # Define parameter grids for the sweep
    Esyn_values = [0.5,-0.5]

    gfast_values = [0.01]
    Vfast_values = [0]
    sfast_values = [20]

    gslow_values = [0.01]
    Vslow_values = [0.0005,0.00005]
    sslow_values = [50000]

    # Generate full grid combinations
    param_grid = itertools.product(gfast_values, gslow_values, sfast_values, Vfast_values, Esyn_values, sslow_values, Vslow_values)

    for i, (gfast, gslow, sfast, Vfast, Esyn, sslow, Vslow) in enumerate(param_grid, 1):
        params = {
            "gfast": gfast,
            "gslow": gslow,
            "sfast": sfast,
            "Vfast": Vfast,
            "Esyn": Esyn,
            "sslow": sslow,
            "Vslow": Vslow
        }
        # Unique filename including parameter values
        filename = os.path.join(output_dir,
                                f"config_gf{gfast}_gs{gslow}_sf{sfast}_Vf{Vfast}_Es{Esyn}_ss{sslow}_Vs{Vslow}.yaml")
        generate_yaml(filename, params)

import yaml
import pandas as pd


def datadict_yaml2md(yaml_path: str):

    md_path = yaml_path.replace(".yaml", ".md")

    with open(yaml_path, 'r') as f:
        datadict = yaml.safe_load(f)

    datadict_list = []
    for key, value in datadict.items():
        if value is not None:
            mydict = {"field": key}
            mydict.update(value)
            datadict_list.append(mydict)

    datadict_df = pd.json_normalize(datadict_list)
    datadict_df.to_markdown(buf=md_path)


if __name__ == "__main__":
    datadict_yaml2md("documentation/EP/EP0006DS0015-KA_Dengue_Daily_SUM/datadictionary.yaml")
    datadict_yaml2md("documentation/EP/EP0005DS0014-KA_Dengue_LL/datadictionary.yaml")

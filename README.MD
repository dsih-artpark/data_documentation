# README.MD - catalogue v2.0.0

This repository contains documentation for datasets that have been standardized and are available through the Data Science and Innovation Hub at ARTPARK.

## Usage

To access the data documentation, locate the **DSID** in our [data catalogue] (https://docs.google.com/spreadsheets/d/1ra4AScicNs1u-WeDTMsnpbBc7OJ2nsA1rqWJfWOchhA/edit?usp=sharing). 

If the *Status* of the dataset in the data catalog is set to **"Standardized and in S3"**, you will find the documentation in this repository.

If you are accessing this repository on GitHub, navigate to the respective subfolder corresponding to the first two characters of the **DSID**. Then, find the DSID, which contains a `.md` and/or `.yaml` file with the data documentation.

Alternatively, you can programmatically access the catalog using our in-house `dataio` package's `fetch_documentation_v2` function. Refer to the [dataio documentation](https://github.com/dsih-artpark/dataio).

## What Does the Data Documentation Contain?

The data documentation (available in `.md` and/or `.yaml` formats) includes:
- The name of the dataset file accessed via S3. A **DSID** may contain multiple datasets;
- Corresponding data dictionaries, including variable names, definitions, access type, and default values (if any);
- Additional details, such as a description of the dataset, its source, and notes under the *info* section.

The supplementary *admin* section includes information from our preprocessing and standardization workflows. For more details on these processes, refer to the [epipipeline documentation](https://github.com/dsih-artpark/epipipeline).

---
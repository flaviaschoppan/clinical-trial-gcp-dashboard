# Clinical Trial Safety & GCP Dashboard

**Python | Clinical Trial Data | Safety Monitoring | Good Clinical Practice (GCP)**

A Python-based project under development to simulate clinical trial data and build an interactive dashboard for exploring adverse event reporting, participant safety, site-level monitoring, and data quality within the context of Good Clinical Practice (GCP).

The project aims to combine synthetic clinical trial data generation, structured data validation, and interactive visualizations to demonstrate practical applications of programming and data analytics in clinical research.

**Development status:** In progress (participant and adverse event generator specifications).

All datasets will be entirely synthetic and represent a fictional clinical trial. This project is intended for educational, technical development, and portfolio purposes. It will not use real patient information or serve as a clinically or regulatorily validated monitoring system.

## 1. Project objectives

The project aims to develop a reproducible analytical environment for exploring selected aspects of clinical trial data management and safety monitoring.

Its main objectives are to:

- Generate structured synthetic participant and adverse event datasets.
- Model relationships between participants, study sites, treatment groups, and adverse event records.
- Apply data integrity and consistency checks to simulated clinical data.
- Explore adverse event characteristics, classifications, and reporting timelines.
- Develop interactive visualizations for safety-related data exploration.
- Investigate site-level indicators and potential data quality issues.
- Demonstrate reproducible Python workflows relevant to clinical research and GCP-oriented data review.

The project is designed as a technical demonstration rather than a substitute for clinical monitoring procedures, pharmacovigilance systems, or regulatory safety reporting.

## 2. Development roadmap

The project will be developed incrementally, beginning with the synthetic data foundation.


| Development block                                   | Scope                                                                                          | Status      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------- |
| **Block 01** - **Synthetic Data Generation**        | Participant and adverse event data modeling, generation, integrity checks, and reproducibility | In progress |
| **Block 02 - Dashboard Foundation**                 | Streamlit application structure, dataset integration, navigation, and interactive filters      | Planned     |
| **Block 03** - **Safety Monitoring Analytics**      | Adverse event summaries, safety indicators, and interactive visualizations                     | Planned     |
| **Block 04** - **Site and Data Quality Monitoring** | Site-level comparisons, consistency indicators, and exploratory data quality assessments       | Planned     |
| **Block 05** - **Reporting and Final Validation**   | Data exploration refinements, reporting/export features, testing, and documentation            | Planned     |


The roadmap represents the intended development direction and may be refined as the project progresses. Planned functionality should not be interpreted as already implemented.

## 3. Public repository scope

This repository is the **public portfolio edition** of the Clinical Trial Safety & GCP Dashboard project.

It will provide selected technical documentation, development milestones, project structure, and non-proprietary materials intended to demonstrate the project's design, methodology, and development progress.

The public specification is documented in `src/data/generator.py`, covering the `generate_patient_data(n_patients=150, seed=42)` and `generate_adverse_event_data(df_patients, seed=42)` interfaces. It defines the expected inputs and outputs, participant and adverse event data schemas, and relationships between participant records and adverse events without exposing the executable implementations.

The complete executable implementation, internal simulation logic, configuration parameters, and detailed validation routines will be maintained separately in a private codebase.

Accordingly, the public repository is not intended to provide a fully executable or reproducible version of the complete application.

## 4. Technology stack


| Technology       | Intended application                                                     |
| ---------------- | ------------------------------------------------------------------------ |
| **Python**       | Data generation, processing, validation, and application logic           |
| **pandas**       | Structured clinical trial data modeling and manipulation                 |
| **NumPy**        | Controlled synthetic data generation and reproducibility                 |
| **Streamlit**    | Planned interactive dashboard interface                                  |
| **Plotly**       | Planned interactive data visualizations                                  |
| **Git / GitHub** | Version control, development history, and public technical documentation |




## 5. GCP and Clinical research context

Good Clinical Practice provides an ethical and quality framework for the design, conduct, recording, and reporting of clinical trials.

Within this context, reliable data structures, traceability, consistency, and accurate safety information are relevant to clinical research workflows.

This project will explore selected technical concepts related to these areas through simulated clinical trial data and reproducible analytical workflows.

The dashboard is not designed to establish GCP compliance, replace investigator or sponsor responsibilities, or perform validated regulatory safety reporting.

## 6. Data privacy and project limitations

The project will use fictional study sites, participants, treatment groups, and adverse event records.

It is intended for software development, methodological exploration, and demonstration of technical skills. It will not use identifiable patient information, represent an actual clinical trial, estimate real treatment effects, or provide clinical decision support.

## 7. Current development status

**Overall project:** In development.

**Current milestone:** Block 01 (Synthetic Data Generation) - Participant and adverse event generator interfaces, data schemas, and participant-event relationships documented.

**Next development step:** Define adverse event classification domains, clinical interpretation rules, and temporal constraints.

This README will be updated as additional development milestones are completed.
from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class ItalianLinguisticAcceptabilityClassification(AbsTaskClassification):
    superseded_by = "Itacola.v2"
    metadata = TaskMetadata(
        name="Itacola",
        dataset={
            "path": "gsarti/itacola",
            "revision": "f8f98e5c4d3059cf1a00c8eb3d70aa271423f636",
            "trust_remote_code": True,
        },
        description="An Italian Corpus of Linguistic Acceptability taken from linguistic literature with a binary annotation made by the original authors themselves.",
        reference="https://aclanthology.org/2021.findings-emnlp.250/",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["ita-Latn"],
        main_score="accuracy",
        date=("2021-01-01", "2021-12-31"),
        domains=["Non-fiction", "Spoken", "Written"],
        dialect=[],
        task_subtypes=["Linguistic acceptability"],
        license="not specified",
        annotations_creators="expert-annotated",
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{trotta-etal-2021-monolingual-cross,
  address = {Punta Cana, Dominican Republic},
  author = {Trotta, Daniela  and
Guarasci, Raffaele  and
Leonardelli, Elisa  and
Tonelli, Sara},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2021},
  doi = {10.18653/v1/2021.findings-emnlp.250},
  month = nov,
  pages = {2929--2940},
  publisher = {Association for Computational Linguistics},
  title = {Monolingual and Cross-Lingual Acceptability Judgments with the {I}talian {C}o{LA} corpus},
  url = {https://aclanthology.org/2021.findings-emnlp.250},
  year = {2021},
}
""",
    )

    def dataset_transform(self):
        self.dataset = (
            self.dataset.rename_columns({"acceptability": "label"})
            .rename_columns({"sentence": "text"})
            .remove_columns(["unique_id", "source"])
        )


class ItalianLinguisticAcceptabilityClassificationV2(AbsTaskClassification):
    metadata = TaskMetadata(
        name="Itacola.v2",
        dataset={
            "path": "mteb/italian_linguistic_acceptability",
            "revision": "4550151a0f0433e65df172c088427063e376ce81",
        },
        description="""An Italian Corpus of Linguistic Acceptability taken from linguistic literature with a binary annotation made by the original authors themselves.
        This version corrects errors found in the original data. For details, see [pull request](https://github.com/embeddings-benchmark/mteb/pull/2900)""",
        reference="https://aclanthology.org/2021.findings-emnlp.250/",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["ita-Latn"],
        main_score="accuracy",
        date=("2021-01-01", "2021-12-31"),
        domains=["Non-fiction", "Spoken", "Written"],
        dialect=[],
        task_subtypes=["Linguistic acceptability"],
        license="not specified",
        annotations_creators="expert-annotated",
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{trotta-etal-2021-monolingual-cross,
  address = {Punta Cana, Dominican Republic},
  author = {Trotta, Daniela  and
Guarasci, Raffaele  and
Leonardelli, Elisa  and
Tonelli, Sara},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2021},
  doi = {10.18653/v1/2021.findings-emnlp.250},
  month = nov,
  pages = {2929--2940},
  publisher = {Association for Computational Linguistics},
  title = {Monolingual and Cross-Lingual Acceptability Judgments with the {I}talian {C}o{LA} corpus},
  url = {https://aclanthology.org/2021.findings-emnlp.250},
  year = {2021},
}
""",
        adapted_from=["ItalianLinguisticAcceptabilityClassification"],
    )

import pandas as pd
from celescope.tools import utils
from celescope.tools.step import Step


PVAL_CUTOFF = 0.05


def read_tsne(tsne_file):
    df = pd.read_csv(tsne_file, sep="\t")
    # compatible with old version
    if "Unnamed: 0" in df.columns:
        df.rename(columns={"Unnamed: 0": "barcode"}, inplace=True)
        df = df.set_index("barcode")
    return df


def format_df_marker(df_marker):
    avg_logfc_col = "avg_log2FC"  # seurat 4
    if "avg_logFC" in df_marker.columns:  # seurat 2.3.4
        avg_logfc_col = "avg_logFC"
    df_marker = df_marker.loc[
        :, ["cluster", "gene", avg_logfc_col, "pct.1", "pct.2", "p_val_adj"]
    ]
    df_marker["cluster"] = df_marker["cluster"].apply(lambda x: f"cluster {x}")
    df_marker = df_marker[df_marker["p_val_adj"] < PVAL_CUTOFF]

    return df_marker


class Report_runner(Step):
    def __init__(self, args, display_title=None):
        super().__init__(args, display_title=display_title)

    def add_marker_help(self):
        self.add_help_content(
            name="Marker Genes by Cluster",
            content="differential expression analysis based on the non-parameteric Wilcoxon rank sum test",
        )
        self.add_help_content(
            name="avg_log2FC",
            content="log fold-change of the average expression between the cluster and the rest of the sample",
        )
        self.add_help_content(
            name="pct.1",
            content="The percentage of cells where the gene is detected in the cluster",
        )
        self.add_help_content(
            name="pct.2",
            content="The percentage of cells where the gene is detected in the rest of the sample",
        )
        self.add_help_content(
            name="p_val_adj",
            content="Adjusted p-value, based on bonferroni correction using all genes in the dataset",
        )

    @staticmethod
    def get_df_file(match_dir):
        """
        return df_tsne_file, df_marker_file
        """
        match_dict = utils.parse_match_dir(match_dir)
        df_tsne_file = match_dict["tsne_coord"]
        df_marker_file = match_dict.get("markers", None)
        return df_tsne_file, df_marker_file

    def get_df(self):
        """
        return df_tsne, df_marker
        """
        if utils.check_arg_not_none(self.args, "match_dir"):
            df_tsne_file, df_marker_file = self.get_df_file(self.args.match_dir)
        elif utils.check_arg_not_none(self.args, "tsne_file"):
            df_tsne_file = self.args.tsne_file
            df_marker_file = self.args.df_marker_file
        else:
            raise ValueError("match_dir or tsne_file must be specified")
        df_tsne = read_tsne(df_tsne_file)
        if df_marker_file:
            df_marker = pd.read_csv(df_marker_file, sep="\t")
            df_marker = format_df_marker(df_marker)
        else:
            df_marker = None
        return df_tsne, df_marker

    def run(self):
        pass

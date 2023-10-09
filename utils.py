# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def top_label(df, label):
    """
    Calculates the top label (reason, demand or action) based on the given dataframe and label.

    Parameters:
    df (pandas.DataFrame): The dataframe containing the data to be analyzed.
    label (str): The label to be used for calculating the top label.

    Returns:
    int: The percentage of the top label in the dataframe.
    """
    top_label_row = df.sort_values('total', ascending=False).iloc[0]
    top_label = top_label_row[label]
    top_label_total = top_label_row['total']
    total_label_total = df['total'].sum()
    top_label_percentage = (top_label_total / total_label_total) * 100
    top_label_percentage = int(round(top_label_percentage))
    return top_label_percentage, top_label


def total_to_percentage(df, total_col):
    # Convert 'total' to percentages
    total = df[total_col].sum()
    df.loc[:, 'percentage'] = (df[total_col] / total) * 100

    return df
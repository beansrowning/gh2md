BASE = r"""Export of Github issues for [{repo_name}]({repo_url}).{datestring}

{issues}
"""

ISSUE = r"""# [\#{number}]({url}) `{state}`: {title}
{labels}
#### <img src="{avatar_url}" width="50">[{author}]({author_url}) opened issue on [[{date}]]:

#### Task
{check_status} #task #gh-automated [#{number}: {title}]({url}) {open_date} {done_status}

{body}

{comments}


-------------------------------------------------------------------------------
"""

COMMENT = r"""#### <img src="{avatar_url}" width="50">[{author}]({author_url}) commented at [{date}]({url}):

{body}
"""

ISSUE_FILE_FOOTNOTE = r"""
[[{repo_name}]]

Export of Github issue for [{repo_name}]({repo_url})
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
from core.documentation import check_freshness
files = [Path(__file__).parents[1] / 'scripts/core/state_store.py', Path(__file__).parents[1] / 'scripts/core/state_machine.py', Path(__file__).parents[1] / 'scripts/core/visualize.py', Path(__file__).parents[1] / 'scripts/core/documentation.py']
report = check_freshness(files, Path(__file__).parents[1] / 'references/harness-api.md')
print(report)
if not report['ok']:
    raise SystemExit(1)

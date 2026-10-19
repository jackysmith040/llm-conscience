from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
from core.documentation import check_freshness
root=Path(__file__).parents[1]
files=list((root/'scripts/core').glob('*.py'))+list((root/'scripts/plugins').glob('*.py'))
report=check_freshness(files, root/'references/animation-engine-api.md')
print(report)
if not report['ok']:
    raise SystemExit(1)

#!/bin/bash
set -e
SKILLS_DIR="/app/skills"

echo ">>> Cloning Indian repos..."

mkdir -p "$SKILLS_DIR/indian-trading" "$SKILLS_DIR/methodology" "$SKILLS_DIR/options-tools" "$SKILLS_DIR/custom"

# gnkbhuvan - NSE stock analysis (11 skills)
git clone --depth=1 https://github.com/gnkbhuvan/nse-stock-analysis-skills /tmp/gnkbhuvan
cp -r /tmp/gnkbhuvan/skills/. "$SKILLS_DIR/indian-trading/"
rm -rf /tmp/gnkbhuvan

# AnshuAgrawal01 - India equity research (20 skills)
git clone --depth=1 https://github.com/AnshuAgrawal01/india-equity-research /tmp/anshu
cp -r /tmp/anshu/equity-research/skills/. "$SKILLS_DIR/indian-trading/"
cp -r /tmp/anshu/financial-analysis/skills/. "$SKILLS_DIR/indian-trading/"
rm -rf /tmp/anshu

# vishalmdi - claude skills (2 skills)
git clone --depth=1 https://github.com/vishalmdi/claude-skills /tmp/vishal
cp -r /tmp/vishal/skills/. "$SKILLS_DIR/indian-trading/"
rm -rf /tmp/vishal

# RupeezyTech - algo ai skill (1 skill)
git clone --depth=1 https://github.com/RupeezyTech/algo_ai_skill /tmp/rupeezy
mkdir -p "$SKILLS_DIR/indian-trading/indian-algo-trading"
cp /tmp/rupeezy/plugins/indian-algo-trading/skills/indian-algo-trading/SKILL.md "$SKILLS_DIR/indian-trading/indian-algo-trading/"
rm -rf /tmp/rupeezy

# mak-thevar - NSELens (1 skill)
git clone --depth=1 https://github.com/mak-thevar/NSELens /tmp/nselens
mkdir -p "$SKILLS_DIR/indian-trading/nse-lens"
cp /tmp/nselens/SKILL.md "$SKILLS_DIR/indian-trading/nse-lens/"
rm -rf /tmp/nselens

# praveenp1118 - Indices Prediction (1 skill)
git clone --depth=1 https://github.com/praveenp1118/Indices-Prediction-Skill-Based-Model /tmp/praveen
mkdir -p "$SKILLS_DIR/indian-trading/indices-prediction"
cp /tmp/praveen/SKILL.md "$SKILLS_DIR/indian-trading/indices-prediction/"
rm -rf /tmp/praveen

# itechsk - Indian Intraday Mentor (1 skill)
git clone --depth=1 "https://github.com/itechsk/-Indian-Intraday-Trading-Mentor" /tmp/intraday
mkdir -p "$SKILLS_DIR/indian-trading/intraday-mentor"
cp /tmp/intraday/SKILL.md "$SKILLS_DIR/indian-trading/intraday-mentor/"
rm -rf /tmp/intraday

# sunnywilson93 - Nifty Options Analysis (1 skill)
git clone --depth=1 https://github.com/sunnywilson93/nifty-options-analysis /tmp/niftyopt
mkdir -p "$SKILLS_DIR/indian-trading/nifty-options-analysis"
cp /tmp/niftyopt/SKILL.md "$SKILLS_DIR/indian-trading/nifty-options-analysis/"
rm -rf /tmp/niftyopt

echo ">>> Cloning tradermonty methodology skills (25 skills)..."
git clone --depth=1 https://github.com/tradermonty/claude-trading-skills /tmp/tradermonty

KEEP_MONTY=(
  backtest-expert breakout-trade-planner downtrend-duration-analyzer
  edge-candidate-agent edge-concept-synthesizer edge-hint-extractor
  edge-pipeline-orchestrator edge-signal-aggregator edge-strategy-designer
  edge-strategy-reviewer exposure-coach macro-regime-detector
  market-breadth-analyzer market-environment-analysis market-top-detector
  portfolio-manager position-sizer scenario-analyzer signal-postmortem
  strategy-pivot-designer technical-analyst theme-detector
  trade-hypothesis-ideator trader-memory-core uptrend-analyzer
)

for skill in "${KEEP_MONTY[@]}"; do
  if [ -d "/tmp/tradermonty/skills/$skill" ]; then
    cp -r "/tmp/tradermonty/skills/$skill" "$SKILLS_DIR/methodology/"
    echo "  + $skill"
  fi
done
rm -rf /tmp/tradermonty

echo ">>> Cloning staskh options/TA skills (7 skills)..."
git clone --depth=1 https://github.com/staskh/trading_skills /tmp/staskh

KEEP_STASKH=(
  greeks spread-analysis technical-analysis
  whale-hunting risk-assessment scanner-pmcc news-sentiment
)

for skill in "${KEEP_STASKH[@]}"; do
  if [ -d "/tmp/staskh/.claude/skills/$skill" ]; then
    cp -r "/tmp/staskh/.claude/skills/$skill" "$SKILLS_DIR/options-tools/"
    echo "  + $skill"
  fi
done
rm -rf /tmp/staskh

echo ""
echo ">>> Done cloning skills."

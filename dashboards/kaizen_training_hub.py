"""
Renders the Continuous Improvement & Knowledge Hub.

This module serves as a central repository for documenting continuous improvement
(Kaizen) events and for hosting training materials related to quality principles.
It supports the MBB's role in coaching, mentoring, and fostering a culture of
quality by sharing successes and enabling skill development.

SME Overhaul (Kaizen Leader Edition):
- The content has been fully populated with academic-grade, actionable materials
  that reflect the principles of Lean (Imai, Shingo, Ohno) and Six Sigma (Deming).
- The Kaizen Event Log is now structured to mirror A3 Thinking, providing deep
  insights into the problem-solving process, with realistic 'redacted' content.
- The Training Library is now a comprehensive curriculum with detailed descriptions,
  learning objectives, and references to foundational literature.
- The UI/UX has been completely redesigned for a professional, engaging, and
  authoritative "knowledge base" feel, using modern layouts and better visual hierarchy.
- All text has been rewritten to inspire action, promote a learning culture,
  and articulate the 'Why' behind continuous improvement.
"""

import logging
import pandas as pd
import streamlit as st

# SME FIX: Import SessionStateManager to resolve the NameError.
# This class is needed for the type hint in the function signature.
from six_sigma.data.session_state_manager import SessionStateManager


# In a real application, this data would come from the SessionStateManager.
# For this overhaul, we define it here to showcase the rich, academic-grade content.

def get_overhauled_kaizen_data():
    """Generates realistic, detailed Kaizen event data."""
    return [
        {
            "id": "KZN-02",
            "title": "SMED on Stamping Press P-101",
            "site": "Andover, US",
            "date": "2025-06-15",
            "problem_background": "The Stamping Press P-101 has an average changeover time of 55 minutes, causing significant production downtime and limiting our ability to run smaller, more flexible batch sizes. This fails to meet the operational target of <15 minutes.",
            "analysis_and_countermeasures": """
            - **Analysis:** A Gemba walk and video analysis (based on Shigeo Shingo's SMED methodology) revealed that 70% of changeover activities were 'internal' (machine stopped). Key opportunities included pre-staging dies, standardizing tools, and eliminating manual adjustments.
            - **Countermeasures Implemented:**
                1.  **Converted Internal to External:** Designed a pre-heating cart for the next die set.
                2.  **Standardized Clamping:** Replaced multi-size bolts with standardized, quick-release clamps.
                3.  **Introduced Poka-Yoke:** Added alignment pins to the die-set to eliminate measurement adjustments.
                4.  **Created Standard Work:** Developed a one-page visual guide for the 2-person changeover team.
            """,
            "quantified_results": "Reduced average changeover time from 55 minutes to 9 minutes (an 83% reduction). This unlocked an additional 120 minutes of production capacity per day and enabled an immediate move to a 'pull' system for downstream assembly.",
            "key_insight": "The biggest gains came not from operators working faster, but from eliminating entire steps of the process. True efficiency is in the design of the work itself, not the effort of the worker."
        },
        {
            "id": "KZN-01",
            "title": "5S Implementation in Main Assembly Cell",
            "site": "Eindhoven, NL",
            "date": "2025-05-22",
            "problem_background": "The Main Assembly cell was experiencing frequent micro-stoppages due to operators searching for tools, components, and fixtures. This introduced significant variability into the Takt time and was a source of operator frustration.",
            "analysis_and_countermeasures": """
            - **Analysis:** A spaghetti diagram of operator movement during a single shift revealed over 400 meters of unnecessary walking. The root cause was a lack of standardized locations for tools and materials.
            - **Countermeasures Implemented (5S):**
                1.  **Sort:** Red-tagged all non-essential items; 3 skids of clutter were removed.
                2.  **Set in Order:** Created shadow boards for all hand tools. Implemented a color-coded bin system for fasteners.
                3.  **Shine:** Conducted a deep clean and established a daily 5-minute cleaning schedule.
                4.  **Standardize:** Laminated standard work instructions for tool placement and end-of-shift cleanup.
                5.  **Sustain:** Added 5S adherence to the daily Gemba walk checklist and supervisor standard work.
            """,
            "quantified_results": "Eliminated 95% of 'searching' time, reducing average assembly time by 15%. Operator-reported ergonomic strain and frustration decreased significantly, confirmed by a post-event survey (results redacted for privacy).",
            "key_insight": "A clean and organized workplace is not about aesthetics; it is a prerequisite for quality and efficiency. When everything has a place, deviations from standard become immediately visible."
        },
        {
            "id": "KZN-04", "title": "Invoice Processing Lead Time Reduction", "site": "Corporate HQ", "date": "2025-07-20",
            "problem_background": "The average lead time from invoice receipt to payment approval is 18 days, causing late payment fees and straining supplier relationships. The goal was to reduce this to <5 days by eliminating non-value-added steps.",
            "analysis_and_countermeasures": """
            - **Analysis:** A detailed process map and swimlane diagram revealed significant 'waiting' waste. 80% of the lead time was spent in queues awaiting manual review, data entry into three separate systems, and manager approval.
            - **Countermeasures Implemented:**
                1.  **Eliminated Redundant Data Entry:** Utilized robotic process automation (RPA) to sync data between systems after initial entry.
                2.  **Established Standard Work:** Created a clear policy for approval thresholds, empowering clerks to approve payments below $5,000 without manager sign-off.
                3.  **Visual Management:** Implemented a digital Kanban board (To Do, In Progress, Done) for full visibility of the invoice workload.
            """,
            "quantified_results": "Reduced average lead time from 18 days to 3.5 days. Eliminated all late payment fees in the first quarter post-implementation, saving an estimated $120k annually.",
            "key_insight": "Lean principles are not just for the factory floor. Transactional processes are often filled with the most 'hidden' waste, offering huge opportunities for improvement."
        },
        {
            "id": "KZN-03", "title": "Root Cause Analysis (RCA) of Intermittent Sensor Failures", "site": "Shanghai, CN", "date": "2025-07-01",
            "problem_background": "The final test stage for the Affiniti Ultrasound system was experiencing a 4% failure rate due to intermittent 'Signal Lost' errors from a key pressure sensor, causing costly rework and diagnostic time.",
            "analysis_and_countermeasures": """
            - **Analysis:** An Ishikawa (Fishbone) diagram was used to brainstorm potential causes. The '5 Whys' technique was then applied to the most likely cause, 'Incorrect Connector Seating'.
                1. **Why?** The connector was not fully seated.
                2. **Why?** The operator could not get enough leverage.
                3. **Why?** The access angle was awkward.
                4. **Why?** A new bracket was installed in a previous update.
                5. **Why? (Root Cause)** The bracket design did not account for tool clearance for the sensor connector.
            - **Countermeasure Implemented:** A cross-functional team of engineering and manufacturing redesigned the bracket with an access cutout. A torque-limiting screwdriver with an audible 'click' was also introduced as a Poka-Yoke.
            """,
            "quantified_results": "Reduced the specific 'Signal Lost' failure rate from 4% to 0.1% within one week of implementation. Rework costs were reduced by an estimated $250k annually.",
            "key_insight": "Technical problems are often symptoms of process or design flaws. Persistently asking 'Why' moves the team beyond blaming components or people to fixing the underlying system."
        }
    ]

def get_overhauled_training_data():
    """Generates a comprehensive, academic-grade training library."""
    return [
        {
            "id": "TRN-101",
            "title": "A3 Thinking: The Art of Problem Solving on a Single Page",
            "type": "eLearning",
            "duration_hr": 2.5,
            "target_audience": "Engineers, Team Leads, Managers",
            "link": "#",
            "icon": "📝",
            "description": "This module explores the Toyota Production System's powerful A3 methodology, which structures problem-solving into a narrative format on a single sheet of A3-sized paper. It is a tool for mentorship, clear communication, and data-driven decision making.",
            "learning_objectives": [
                "Understand the 7 sections of a standard A3 Report.",
                "Frame a problem statement effectively.",
                "Use the PDCA (Plan-Do-Check-Act) cycle within the A3 framework.",
                "Visually communicate root cause analysis and countermeasures."
            ],
            "recommended_reading": "'Managing to Learn' by John Shook"
        },
        {
            "id": "TRN-102",
            "title": "Statistical Process Control (SPC) Masterclass",
            "type": "Workshop Slides",
            "duration_hr": 8.0,
            "target_audience": "Quality Engineers, Process Technicians",
            "link": "#",
            "icon": "📊",
            "description": "A deep dive into the principles of Dr. W. Edwards Deming and Walter Shewhart. This workshop provides the statistical foundation for understanding process variation, distinguishing between common and special causes, and using control charts to monitor and improve process stability.",
            "learning_objectives": [
                "Calculate control limits for I-MR, Xbar-R, and p-charts.",
                "Interpret control chart signals (e.g., Nelson Rules).",
                "Define and calculate process capability indices (Cp, Cpk).",
                "Understand the relationship between process control and process capability."
            ],
            "recommended_reading": "'Understanding Variation: The Key to Managing Chaos' by Donald J. Wheeler"
        },
        {
            "id": "TRN-103",
            "title": "Leading Kaizen Events: A Facilitator's Guide",
            "type": "PDF Guide",
            "duration_hr": 4.0,
            "target_audience": "MBB, Black Belts, CI Leads",
            "link": "#",
            "icon": "🤝",
            "description": "This guide provides a practical, step-by-step framework for planning, executing, and sustaining a successful week-long Kaizen event. It covers team selection, scoping, daily management, and follow-up activities to ensure that improvements are not only made but also maintained.",
            "learning_objectives": [
                "Develop a compelling Kaizen charter.",
                "Manage team dynamics and engage stakeholders.",
                "Facilitate brainstorming and root cause analysis sessions.",
                "Establish a 30-day follow-up plan to ensure sustainability."
            ],
            "recommended_reading": "'Kaizen: The Key to Japan's Competitive Success' by Masaaki Imai"
        },
        {
            "id": "TRN-104", "title": "Failure Mode and Effects Analysis (FMEA)", "type": "eLearning", "duration_hr": 3.0, "target_audience": "Engineering, R&D, Quality", "link": "#", "icon": "🛡️",
            "description": "Learn to proactively identify and mitigate risks in product and process design. This module teaches the systematic approach of FMEA to anticipate potential failures, assess their impact, and implement robust controls before problems reach the customer.",
            "learning_objectives": ["Distinguish between Design FMEAs and Process FMEAs.", "Calculate Risk Priority Numbers (RPN).", "Develop effective detection and prevention controls.", "Integrate FMEA into the product development lifecycle."],
            "recommended_reading": "'The FMEA Pocket Handbook' by D. H. Stamatis"
        },
        {
            "id": "TRN-105", "title": "Value Stream Mapping (VSM)", "type": "Workshop Slides", "duration_hr": 6.0, "target_audience": "Operations, CI Leads, Management", "link": "#", "icon": "🌊",
            "description": "This workshop teaches you how to see the flow of value and, more importantly, the flow of waste. Learn to create current-state and future-state maps that visualize not just material flow, but information flow, to design truly lean systems from end to end.",
            "learning_objectives": ["Identify a value stream and its product family.", "Calculate key metrics like Lead Time, Process Time, and Process Cycle Efficiency.", "Draw current-state and future-state maps using standard iconography.", "Develop a Kaizen-based implementation plan."],
            "recommended_reading": "'Learning to See' by Mike Rother and John Shook"
        }
    ]

def get_glossary_content():
    """Generates the content for the methodologies and terminology glossary."""
    return {
        "Lean Principles": [
            {"term": "Takt Time", "definition": "The rate at which a finished product needs to be completed to meet customer demand. It is the 'heartbeat' of a lean system.", "formula": r"Takt\ Time = \frac{\text{Available Production Time per Day}}{\text{Customer Demand per Day}}"},
            {"term": "Gemba (現場)", "definition": "Japanese for 'the real place.' It refers to the location where value is created, such as the factory floor or a service desk."},
            {"term": "Kaizen (改善)", "definition": "A strategy of 'Continuous Improvement' where small, ongoing, positive changes are made to a process. It emphasizes employee involvement and a culture of incremental enhancement."},
            {"term": "Muda (無駄), Mura (斑), Muri (無理)", "definition": "The '3 M's' of waste in the Toyota Production System. **Muda:** Non-value-added waste. **Mura:** Unevenness or irregularity. **Muri:** Overburdening equipment or operators."},
            {"term": "Muda (無駄)", "definition": "Japanese for 'waste.' It refers to any activity that consumes resources but creates no value for the customer. The 7 classic wastes are: Transport, Inventory, Motion, Waiting, Overproduction, Over-processing, and Defects (TIMWOOD)."},
            {"term": "Jidoka (自働化)", "definition": "Autonomation or 'automation with a human touch.' The principle of designing equipment to stop automatically and signal immediately when a problem occurs, preventing the mass production of defects."},
            {"term": "Heijunka (平準化)", "definition": "Production leveling. The process of smoothing the type and quantity of production over a fixed period. This reduces Mura (unevenness) and minimizes inventory."},
            {"term": "Kanban (看板)", "definition": "A scheduling system for lean manufacturing and just-in-time manufacturing (JIT). It is a visual signal (e.g., a card) that triggers an action, such as replenishing a part."},
            {"term": "Poka-Yoke (ポカヨケ)", "definition": "A 'mistake-proofing' mechanism. Any technique in a process that helps to avoid errors by preventing, correcting, or drawing attention to them as they occur."},
            {"term": "Value Stream Mapping (VSM)", "definition": "A flowchart method used to visualize, analyze, and improve all the steps in a product delivery process, from raw materials to the customer. It helps identify and eliminate waste (Muda)."},
            {"term": "5S", "definition": "A workplace organization method based on five Japanese words: Seiri (Sort), Seiton (Set in Order), Seisō (Shine), Seiketsu (Standardize), and Shitsuke (Sustain)."}
        ],
        "Six Sigma Concepts": [
            {"term": "DMAIC", "definition": "The core data-driven improvement cycle: **D**efine the problem, **M**easure key aspects of the current process, **A**nalyze the data to investigate root causes, **I**mprove the process, and **C**ontrol the future state."},
            {"term": "DPMO (Defects Per Million Opportunities)", "definition": "A key metric for process performance. It represents the number of defects in a process per one million opportunities. A Six Sigma process aims for 3.4 DPMO.", "formula": r"DPMO = \frac{\text{Number of Defects}}{\text{Number of Units} \times \text{Opportunities per Unit}} \times 1,000,000"},
            {"term": "Process Capability (Cp)", "definition": "Measures the potential capability of a process, assuming it is perfectly centered between the specification limits. It answers: 'Is the process spread narrow enough?'", "formula": r"C_p = \frac{USL - LSL}{6\sigma}"},
            {"term": "Process Capability (Cpk)", "definition": "Measures the actual capability of a process, accounting for its centering. It represents the 'worst-case' side of the process distribution. A Cpk of >1.33 is often a minimum target.", "formula": r"C_{pk} = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)"},
            {"term": "COPQ (Cost of Poor Quality)", "definition": "The total financial loss incurred from producing defective products or services. Includes internal failure costs (scrap, rework) and external failure costs (warranty claims, returns)."},
            {"term": "Voice of the Customer (VOC)", "definition": "The process of capturing customer expectations, preferences, and aversions. The VOC is translated into Critical-to-Quality (CTQ) requirements for the process."},
            {"term": "Rolled Throughput Yield (RTY)", "definition": "The probability that a multi-step process will produce a defect-free unit. It is the product of the First Time Yields (FTY) of each process step.", "formula": r"RTY = FTY_1 \times FTY_2 \times \dots \times FTY_n"},
        ],
        "Statistical & Analytical Methods": [
            {"term": "Control Chart Limits", "definition": "The horizontal lines on a control chart (UCL/LCL) that represent the 'voice of the process.' They are calculated from the process data and typically set at ±3 standard deviations from the center line.", "formula": r"UCL/LCL = \mu \pm 3\sigma"},
            {"term": "Hypothesis Testing", "definition": "A formal statistical procedure used to accept or reject a claim about a process or population based on sample data. It involves a Null Hypothesis (H₀, the status quo) and an Alternative Hypothesis (Hₐ)."},
            {"term": "p-value", "definition": "The probability of obtaining test results at least as extreme as the results actually observed, assuming the null hypothesis is correct. A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis."},
            {"term": "ANOVA (Analysis of Variance)", "definition": "A statistical test used to determine whether there are any statistically significant differences between the means of two or more independent groups."},
            {"term": "Confidence Interval", "definition": "A range of values, derived from sample statistics, that is likely to contain the value of an unknown population parameter. A 95% confidence interval means we are 95% confident the true population mean lies within that range."},
            {"term": "Gage R&R (Repeatability & Reproducibility)", "definition": "A statistical study to evaluate the precision of a measurement system. **Repeatability** is the variation from the same operator using the same tool. **Reproducibility** is the variation between different operators using the same tool."},
            {"term": "Regression Analysis", "definition": "A set of statistical processes for estimating the relationships between a dependent variable (the 'output' or 'Y') and one or more independent variables (the 'inputs' or 'X's')."},
            {"term": "Design of Experiments (DOE)", "definition": "A systematic method to determine the relationship between factors affecting a process and the output of that process. Used to find the optimal 'recipe' for a process with minimal experimental runs."}
        ],
        "AI/ML for Operations": [
            {"term": "Supervised Learning", "definition": "A type of machine learning where the model learns from data that has been manually labeled with the correct outcomes. Analogy: Learning with an 'answer key.' (e.g., training a model on historical data of 'Pass' vs. 'Fail' parts)."},
            {"term": "Unsupervised Learning", "definition": "A type of machine learning where the model works on its own to discover patterns and information in unlabeled data. Analogy: Finding hidden groups without an answer key. (e.g., K-Means clustering to find different failure modes)."},
            {"term": "Isolation Forest", "definition": "An unsupervised algorithm excellent for anomaly detection. It works by 'isolating' outliers, which are easier to separate from the main data cluster."},
            {"term": "Random Forest", "definition": "A powerful supervised learning algorithm that is an 'ensemble' of many individual decision trees. It averages their predictions to produce a more accurate and stable result. Excellent for predictive quality tasks."},
            {"term": "SHAP (SHapley Additive exPlanations)", "definition": "A game-theoretic approach used to explain the output of any machine learning model. It connects optimal credit allocation with local explanations to understand *why* a model made a specific prediction for a single instance."}
        ]
    }

logger = logging.getLogger(__name__)

def render_kaizen_training_hub(ssm: SessionStateManager) -> None:
    """Creates the UI for the Continuous Improvement & Knowledge Hub."""
    st.header("🎓 Continuous Improvement & Knowledge Hub")
    st.markdown("""
    Welcome to the central nervous system of our learning organization. This hub is the catalyst for our Continuous Improvement (CI) culture.
    Here, we **celebrate our successes**, **share our wisdom**, and **empower our teams** with the knowledge to drive process excellence.
    """)

    try:
        # --- 1. Load Data ---
        # NOTE: For a fully integrated system, this data should be moved into
        # the SessionStateManager and accessed via ssm.get_data(). For this
        # showcase, we use local functions to provide rich content.
        kaizen_events = get_overhauled_kaizen_data()
        training_materials = get_overhauled_training_data()
        glossary = get_glossary_content()

        st.info("Select a tab to review the A3 reports from past Kaizen events or to access our curated library of quality and CI training.", icon="🧠")
        events_tab, training_tab, glossary_tab = st.tabs(["🏆 **Kaizen Event A3 Log**", "📚 **Training & Development Library**", "📖 **Methodologies & Terminology Glossary**"])

        # ==================== KAIZEN EVENT LOG ====================
        with events_tab:
            st.subheader("Implementing Kaizen: A Chronicle of Realized Improvements")
            st.markdown("Each event below is a testament to a team's dedication to making our work better. Review these A3 summaries to understand the 'Why' behind the change and to find inspiration for your own area.")

            if not kaizen_events:
                st.warning("No Kaizen events have been logged in the data model.")
            else:
                df_events = pd.DataFrame(kaizen_events).sort_values(by='date', ascending=False)
                for _, event in df_events.iterrows():
                    with st.container(border=True):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.markdown(f"#### {event['title']}")
                            st.caption(f"**A3 ID:** {event['id']} | **Site:** {event['site']} | **Completion Date:** {event['date']}")
                        with col2:
                            st.button("View Full A3 Report", key=f"report_{event['id']}", type="primary", disabled=True, use_container_width=True, help="Full PDF report not available in this demo.")

                        st.markdown("**Problem Background:**")
                        st.markdown(f"> {event['problem_background']}")

                        with st.expander("**View Detailed Analysis & Countermeasures**"):
                            st.markdown(event['analysis_and_countermeasures'])
                            st.caption("_Detailed schematics, raw data, and financial models are redacted from this view and available in the full A3 report._")
                        
                        st.markdown("**Quantified Results:**")
                        st.success(f"{event['quantified_results']}", icon="💡")

                        st.markdown("**Key Insight / Lesson Learned:**")
                        st.info(f"{event['key_insight']}", icon="🔬")

                    st.write("") # Adds vertical space

        # ==================== TRAINING LIBRARY ====================
        with training_tab:
            st.subheader("Empowering Excellence Through Education")
            st.markdown("A commitment to quality begins with a commitment to learning. This curated library provides resources to develop skills at every level of the organization, from foundational principles to advanced statistical methods.")

            if not training_materials:
                st.warning("No training materials are available in the data model.")
            else:
                df_training = pd.DataFrame(training_materials)
                for _, material in df_training.iterrows():
                    st.markdown(f"""
                    <div style="border: 1px solid #c8c8c8; border-left: 6px solid #007bff; border-radius: 8px; padding: 20px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <div style="display: flex; align-items: flex-start;">
                            <span style="font-size: 2.5em; margin-right: 25px; margin-top: 5px;">{material['icon']}</span>
                            <div style="flex-grow: 1;">
                                <div style="font-weight: bold; font-size: 1.2em; margin-bottom: 5px;">{material['title']}</div>
                                <div style="font-size: 0.9em; color: #555; margin-bottom: 15px;">
                                    <span><b>Type:</b> {material['type']}</span> |
                                    <span><b>Est. Duration:</b> {material['duration_hr']} hrs</span> |
                                    <span><b>Primary Audience:</b> {material['target_audience']}</span>
                                </div>
                                <p style="font-size: 1em; color: #333; margin-bottom: 15px;">{material['description']}</p>
                                <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; font-size: 0.9em;">
                                    <b>Learning Objectives:</b>
                                    <ul>{''.join([f"<li>{obj}</li>" for obj in material['learning_objectives']])}</ul>
                                    <b>Recommended Reading:</b> <i>{material['recommended_reading']}</i>
                                </div>
                                <a href="{material['link']}" target="_blank" style="display: inline-block; background-color: #007bff; color: white; padding: 8px 15px; margin-top: 15px; border-radius: 5px; text-decoration: none; font-weight: bold;">Launch Module</a>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
       
        with glossary_tab:
            st.subheader("The Common Language of Continuous Improvement")
            st.markdown("Use this dictionary to understand the key terms, concepts, and methodologies that form the foundation of our operational excellence program. A shared vocabulary is essential for effective collaboration and problem-solving.")

            for category, terms in glossary.items():
                with st.expander(f"**{category}**", expanded=(category == "Lean Principles")):
                    for item in terms:
                        st.markdown(f"**{item['term']}**")
                        st.markdown(f"> {item['definition']}")
                        if 'formula' in item:
                            st.latex(item['formula'])
                        st.write("") # Add a little space
                        
    except Exception as e:
        st.error(f"An error occurred while rendering the Kaizen & Training Hub: {e}")
        logger.error(f"Failed to render kaizen and training hub: {e}", exc_info=True)

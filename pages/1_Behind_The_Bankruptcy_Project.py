import streamlit as st
st.set_page_config(page_icon='✅')

st.image('./pages/media/bankruptcy_header.png', caption='A selection of 2023 bankruptcy filings')
st.code('Last updated: Feb 6, 2024')
st.header("Behind the Bankruptcy Project")
## Motivation
st.write("""
I chose corporate bankruptcy as the topic of my capstone project because it combines a lot of my [background](https://www.linkedin.com/in/markstansky/).  Fundamental credit and equity analysis requires an analyst to understand a company’s effectiveness in sourcing income (revenues) and efficiency at producing cash flows, today as well as into the future.
Financial statements contain troves of data and the ability of machine learning to detect financial patterns unnoticed by the human eye struck me as an ideal application. 

I've also worked at several startups, promising young companies.  Bankruptcy interests me because it is emblematic of the other end of the corporate lifecycle.  That is, what forces have caused or lead to a business' undoing?  What can be learned by those that remain?
""")

## What & Why
st.subheader("Data Sources and Treatment")
st.write("""
My project’s starting point is the [Florida-UCLA-LoPucki Bankruptcy Research Database](https://lopucki.law.ufl.edu/index.php) (note: updates discontinued EO 2022).  

This data served as an excellent reference for past public bankruptcies, however, I found that the supplied historical financials were inconsistently reported throughout the dataset.
Further, the UFL Center for Bankruptcy discontinued the project at the end of 2022, requiring me to identify and add all qualifying 2023 bankruptcy cases.
To gather the comprehensive financial data that my project required, I leveraged the [XBRL API](https://xbrl.us/home/use/xbrl-api/) pulling GAAP financial line items common to all issuers, regardless of industry.
These include items such as Net Income, Cash from Operations, Total Assets, Total Liabilities, etc.

A few callouts and highlights from my data exploration below:
""")

st.subheader('1. XBRL\'s Limitations')
st.write("""
The XBRL standard was phased in by the SEC beginning in 2009 with general compliance achieved by 2013.
With that constraint, I could only acquire a complete 3-year annual financials for 89 cases filed between 2013 and fall 2023.
The Lopucki database originally contained 1,218 entries of large US bankruptcy cases (large defined by BS assets over \$100 MM in 1980 dollars, ~$300M in today's dollars.)
In a future analysis, I'd like to reach back beyond the 2013 boundary to achieve a much richer dataset.
""")
st.image('./pages/media/filings_by_year.jpg')

st.subheader('2. A slide towards insolvency')
st.write("""
Studying the three years of annual financials prior to a filer's bankruptcy, a visible trend towards net loss and cash outflows emerges.
""")
# Point #2 image
st.image('./pages/media/slide_towards_bankruptcy.png', caption='Aggregated annual financials of bankruptcy filers  3, 2, and 1 years prior to default.')


## Clustering Analysis
st.subheader("3. Grouping Bankruptcies in an Unsupervised Manner")
st.write("""
As an analyst, my instinct is to group these companies by industry, time period, or size. 
Since machine learning is adept at detecting patterns in data, I was curious how it would group bankruptcies without any instruction.
My goal in trying this technique was to unearth thematic groupings in bankrupt filer's financials, potentially identifying clusters of similar bankruptcies for future investigation.
I  tried several approaches to prepare the data, employing three dimensionality reduction techniques (PCA, TSNE, and UMAP) and two scaling algorithms (minmax and standard scaling).
The best I found was UMAP under standard scaling.  I split the data into four groups using the K-Means clustering algorithm:
""")
st.image('./pages/media/UMAP_clustering.png')

st.write("""
Interpreting feature statistics of each cluster revealed the following general trends:

**Group 0:**
Small companies in terms of absolute dollar size in all statements (revenue, assets, etc.)

**Group 1:**
Large Companies, defined by highest median revenue, assets, etc. and positive operating cash flow.

**Group 2:**
Companies characterized by large historical losses, but had demonstrated financial improvement leading up to bankruptcy.

**Group 3:**
Companies generating small revenues and large net losses, yet had positive operating cash flow.

It would be a fascinating follow-on analysis to examine each cluster's actual bankruptcy proceedings and to see whether their bankruptcy's causes were similar.
""")





## Predictive?

st.header("Testing Predictiveness on the S&P500")
st.write("""

The ultimate aim of my project is to use this bankruptcy data to predict future financial stress.
If I were to pull the same financial data of constituents in the current S&P 500, could my machine learning model tell the difference between my bankrupt companies and a (currently) living one?
What financial features does the model focus on?  


To try out this theory, I combined my bankrupt and S&P members into one dataset.
The companies varied greatly when measured in absolute dollar size. 
To normalize these differences, I standardized the financial data by computing 37 financial ratios measuring efficiency (margin, turnover, etc.) that would be familiar to any financial analyst.
Splitting this data into test and train groups, I assigned the input, or X data, to the 37 financial ratios I computed.
The Y data is the binary 1 / 0 that records whether the given example is a bankrupt company or not.  The task for each model is to correctly classify whether the example is a 1 or 0.

**Technique 1: Logistic Regression**  

Using the train data, I implemented a Linear Logistic Regression with the default L2 regularization.
I then used the trained logistic regression model to classify each test case in the data.

The logistic regression turned in a bad result, missing 11 out of 16 bankruptcy cases in the test set. 
Notably, the model's F-1 Score of .81, a measure balancing a model's precision and sensitivity, appeared high.
This is explained by the dataset's class-imbalance (500 S&P members vs. 89 bankruptcy cases from the last decade).
By simply guessing "0, not bankrupt" one will guess correctly far more often than not.  

""")
st.image('./pages/media/bankV1_log_reg_cnf.png', caption= 'Logistic Regression Confusion Matrix')

st.write("""
My takeaway: the linear logistic regression model is not sensitive to bankrupt cases at all.  Given the lack of predictiveness, examining model weights doesn't make sense here.

**Technique 2: Decision Tree**  

I tried a second classification technique, a Decision Tree.
The algorithm, trained to efficiently sort bankrupt companies from healthy ones based upon features in the data, performed significantly better and correctly classified 13 out of the 16 bankruptcy cases.
Importantly, the model's sensitivity to bankruptcy cases (recall score) grew from .12 to .81, clearly it can identify a bankrupt company.
This discrepancy in sensitivity between techniques is striking, and indicates that the relationship between my supplied features and our target variable (bankruptcy) is a complex relationship a linear function will struggle to describe.
""")
st.image(['./pages/media/bankV1_DT_tree.png',
          './pages/media/DT_conf_matrix.png'],
         caption= ['Plotted Bankruptcy Decision Tree',
                   'Decision Tree confusion Matrix'],
         )

st.write("""
Given the model's ability to identify bankruptcy cases, it's worth discussing the tree's initial decision points.  
1. 2 YoY Sales growth: whether a company grew over a two year period.  
Simple enough: "was the business growing?"  To be in the 'True' camp, sales growth had to be greater than or equal to .007%, effectively revenue growth over two years that was flat or better.


2. 1Y Solvency (same decision feature for both sides, different value however): current year assets / current year liabilities.
 In the left-hand tree, companies 1 year A/L below ~1.32 were more likely to be insolvent.
 On the right hand tree, companies 

Note that in following this tree down, groups of cases become further qualified by an increasing set of rules.  
E.g. examples in the blue box on the far left of the 3rd layer of the DT, the samples are companies that have flat / negative 2YoY sales growth AND a solvency ratio under ~1.32.

""")

st.subheader('Random Forest: Improving on the Decision Tree')
st.write("""
My Decision Tree model was the most successful tested, however it's accuracy could be suspect in a few ways:
1. The tree was not limited in its depth, and likely overfits to achieve such high accuracy.
2. It's possible I got lucky generating a model that works for this specific data.

Rather than settle for one Decision Tree and to  better generalize to any company my model may analyze, I created a Random Forest Model.
As was done for the Decision Tree, I separated the financial ratios as X features from the bankruptcy outcome and randomized and split my data into training and test groups.
I performed a grid search to test for the appropriate depth that would precisely sort, but not oversort. I concluded a tree-depth of 4 provided the greatest accuracy while minimizing the risk of an overfit model.
""")

st.write("**The first three 'trees' in my Random Forest:**")

st.image(['./pages/media/RF_tree_1.png',
          './pages/media/RF_tree_2.png',
          './pages/media/RF_tree_3.png']
         , width = 300
         )
st.write("""

To be expected from a generalized model, the decision's tree accuracy and sensitivity suffered, the Random Forest correctly classified only 12/20 bankruptcies (a recall of 0.6).
On the upshot, it correctly identified all 88 S&P members in the test set.
It would be an interesting further analysis to examine the misclassified bankruptcies.
Since bankruptcy can occur in unexpected ways, it's possible that some of these cases were not driven by the company's financial fundamentals.  
(Note: in creating the RF model I changed the randomstate parameter during the train test split which resulted in the new test pool having 20 bankrupt cases to test against vs the previous 18.)
""")
st.image('./pages/media/RF_conf_matrix.png')

st.write("""
**Feature Importances**  
Across all decision trees in my random forest, the below features were most used by the model.
I don't find many surprises in the left-most metrics: the top three are sales growth and solvency in the year of bankruptcy.
I think this underscores how impending bankruptcy becomes increasingly visible and apparent in the immediate time period approaching a bankruptcy filing (and likely already reflected in a share price.)
I am somewhat surprised that metrics involving Operating Cash Flow, a measure of funds available to do things like paying down debt, first surfaces as the sixth and tenth most features. 
If I were to run this analysis again, perhaps I would remove the immediate year of financial information from the bankruptcy set, hopefully forcing the model to identify longer term indicators that may be less common and obvious.
I do, though, find it notable that some alternative comparisons I included, for example Financing Cash Flow to Revenue and 3Y-prior Cash to Revenue were among the top 10 metrics.
With further analysis, these ratios may be good indicators of specific bankruptcy scenarios.  
""")
st.image('./pages/media/bankV1_RF_feature_importance.png')



### (Conclusion & Next Steps)
st.subheader("Conclusion and Next Steps")
st.code('“How did you go bankrupt?" \n"Two ways. Gradually, then suddenly.” \n ― Ernest Hemingway, The Sun Also Rises')
st.write("""
As you are likely aware, the interactive component of this project is available in the website sidebar's Interactive Bankruptcy Odds App.
There, you will find an interactive demo allowing you to discover the % likelihood of a S&P 500 member going bankrupt in the next year.

Far more interesting in my opinion is the interactive make-your-own financial statement visualization underneath.
Under the same premise as the bankruptcy predictor, you can supply any company's financials (or those of your own creation) to see whether the model thinks it is a goner.

As will be called out in bullet-point form below, this project made some significant assumptions.
Firstly, the greatest likelihood of bankruptcy for an S&P member was Prudential Group at 40%.
In hindsight, if I were earnestly seeking bankruptcy-candidates, it was silly to analyze S&P members, as opposed to, say, the Russell 2000 where companies are smaller, industry focused, and generally riskier.
After all, the 'blue-chip' nature of the S&P is that they have performed well for a long period of time.
Inclusion in the index requires a full-year of GAAP profitability!

I really enjoyed creating and writing about this analysis, it served as a great way to practice applying machine learning to an industry I know well.
I plan to return to this project to add new companies (Russell 3k) and apply new classification techniques (working on a neural network!)
Several offshoot projects occurred to me while conducting this analysis, which I believe further underscores the abundant opportunity available to apply machine learning in fundamental financial analysis, so please check back soon.
I find the utility of this kind of analysis, and something I made an effort to call out in the above narrative,
would be the thought-provoking nature of data exploration.
I could easily see myself crafting a shortlist of issuers that myself or another analyst could take away to conduct more traditional financial analysis.
""")
st.code('End of article.')

st.write("""
\n
**Notes, Assumptions and Shortcomings**
- It is obvious that companies do not operate in a vacuum, and therefore common Data Science assumptions of data independence, normality of distribution, and equality of variance are compromised.
- A larger database of bankruptcies would be beneficial, particularly from time periods where financial conditions are different from this past decade.
- Noted above, it is assumed that if a S&P 500 company is misclassified, or assigned a relatively high probability of belonging to the bankrupt class, implies it is experiencing similar financial stress to a company in the bankruptcy process.
This could be misleading for some issuers (e.g. newly-listed high growth startups, non-traditional companies, or vehicles like BDCs or REITs)
- It was challenging to determine how to best address the class imbalance between bankrupt companies and the S&P members.  Relative to the world of corporate issuers, bankruptcies are relatively rare.
When training the classification models, correcting for the class imbalance actually produced worse models than leaving it unaddressed.
- Some features may be redundant.  While I used L2 Regression in the Logistic Model, more aggressively pruning features may be able to produce the same (or better) results with less input.  This will be explored in a subsequent analysis.
- It would be worth exploring the "non-linearities" discovered further, perhaps I could've addressed them through using feature cross products to improve the Logistic Regression's performance.
- While leveraging the XBRL standard enabled me to have a large amount of detailed financial data per issuer, the system suffers from issuers' inconsistent tagging practices.
Querying for only GAAP-standard tags solved the lion's share of this issue, but some examples in both the bankruptcy and S&P set were dropped due to incomplete data.
""")
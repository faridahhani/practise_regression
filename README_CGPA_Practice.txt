CGPA Prediction Practice Files

1. Open CGPA_Multiple_Linear_Regression_Practice.ipynb.
2. Keep student_cgpa_synthetic.csv in the same folder as the notebook.
3. Run all notebook cells.
4. The notebook creates cgpa_linear_regression_model.pkl.
5. Keep cgpa_dashboard.py and cgpa_linear_regression_model.pkl in the same folder.
6. Install requirements:
   pip install -r requirements_cgpa.txt
7. Run Streamlit:
   streamlit run cgpa_dashboard.py

Expected model performance for the supplied synthetic dataset:
R-squared approximately 0.681
RMSE approximately 0.213

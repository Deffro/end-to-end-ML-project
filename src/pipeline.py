from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from feature_engine.imputation import (
    CategoricalImputer,
)

from feature_engine.transformation import (
    YeoJohnsonTransformer,
)

from feature_engine.encoding import (
    OrdinalEncoder,
    OneHotEncoder,
    CountFrequencyEncoder
)

from src.config.core import config
from src.processing import features as pp


pipe = Pipeline([
    ('cat_imputer_missing',CategoricalImputer(
        imputation_method='missing', variables=config.model_config.cat_vars_replace_na_with_string_missing)),
    ('cat_imputer_frequent',CategoricalImputer(
        imputation_method='frequent', variables=config.model_config.ca_vars_replace_na_with_frequent)),
    ('num_transformer_yeo_johnson', YeoJohnsonTransformer(
        variables=config.model_config.num_vars_yeo_johnson)),
    ('ordinal_encoder', OrdinalEncoder(
        encoding_method='ordered', variables=config.model_config.cat_vars_ordinal)),
    ('ordinal_encoder_arbitrary', OrdinalEncoder(
        encoding_method='arbitrary', variables=config.model_config.cat_vars_ordinal_arbitrary)),
    ('count_frequency_encoder', CountFrequencyEncoder(
        encoding_method='frequency', variables=config.model_config.cat_vars_count_frequency)),
    ('onehot_encoder', OneHotEncoder(
        variables=config.model_config.cat_vars_onehot)),
    ('experience_map', pp.Mapper(
        variables=config.model_config.experience_var, mappings=config.model_config.experience_map)),
    ('last_new_job_map', pp.Mapper(
        variables=config.model_config.last_new_job_var, mappings=config.model_config.last_new_job_map)),
    ('company_size_map', pp.Mapper(
        variables=config.model_config.company_size_var, mappings=config.model_config.company_size_map)),
    ('min_max_scaler', MinMaxScaler()),
    ('logistic_regression', LogisticRegression(random_state=config.model_config.random_state))
])

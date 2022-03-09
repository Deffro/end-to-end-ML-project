from feature_engine.transformation import YeoJohnsonTransformer

from src.config.core import config


def test_yeo_johnson(all_data):
    assert all_data[config.model_config.num_vars_yeo_johnson].iloc[0].values[0] == 36

    yeo_transformer = YeoJohnsonTransformer(
        variables=config.model_config.num_vars_yeo_johnson
    )
    subject = yeo_transformer.fit_transform(all_data)

    assert (
        subject[config.model_config.num_vars_yeo_johnson].iloc[0].values[0]
        == 4.719119791024215
    )

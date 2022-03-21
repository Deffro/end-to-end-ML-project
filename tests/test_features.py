from feature_engine.transformation import YeoJohnsonTransformer

from src.config.core import config


def test_yeo_johnson(train_data):
    assert train_data[config.model_config.num_vars_yeo_johnson].iloc[0].values[0] == 36

    yeo_transformer = YeoJohnsonTransformer(
        variables=config.model_config.num_vars_yeo_johnson
    )
    subject = yeo_transformer.fit_transform(train_data)

    assert (
        subject[config.model_config.num_vars_yeo_johnson].iloc[0].values[0]
        == 4.719119791024215
    )

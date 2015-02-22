wowapi
======
**Stable:** [![Build Status](https://travis-ci.org/GoblinLedger/wowapi.svg?branch=master)](https://travis-ci.org/GoblinLedger/wowapi)

**Development:** [![Build Status](https://travis-ci.org/GoblinLedger/wowapi.svg?branch=develop)](https://travis-ci.org/GoblinLedger/wowapi)

Installation
------------

```bash
$ pip install wowapi
```

Documentation
-------------

```python
>>> import wowapi
>>> api = wowapi.API('yourApiKeyGoesHere')
>>> api.character('madoran', 'Aisa')
{u'realm': u'Madoran' ...
```

const dataAPIHost = process.env.REACT_APP_DATA_API_HOST || ''

const domain = window.location.origin !== dataAPIHost && dataAPIHost ? dataAPIHost : window.location.origin

const urlPrefix = new URL('api', domain).toString();


const getToken = () => {
  return `Bearer ${window.localStorage.getItem('crypto-token')}`
}

export const getResources = async (resources, history) => {

  const resourcesString = resources.join()

  const url = `${urlPrefix}/resources/${resourcesString}`

  return await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })
    .then(async (res) => {
      if (res.status >= 400) {
        history.replace(history.location.pathname, {
          errorStatusCode: res.status
        });
      } else {
        return res.json()
      }
    })
}


export const getTrades = async (page, pipelineId) => {

  const url = `${urlPrefix}/trades${page ? '/' + page : ''}${pipelineId ? '?pipelineId=' + pipelineId : ''}`

  return await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })
    .then(res => {
      if (res.status >= 400) {
        throw(new Error('Error fetching trades'))
      } else {
        return res.json()
      }
    })
}


export const getPipelines = async (page) => {

  const url = `${urlPrefix}/pipelines${page ? '/' + page : ''}`

  return await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })
    .then(res => {
      if (res.status >= 400) {
        throw(new Error('Error fetching pipelines'))
      } else {
        return res.json()
      }
    })
}


export const getPositions = async (page) => {

  const url = `${urlPrefix}/positions${page ? '/' + page : ''}`

  return await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })
    .then(res => {
      if (res.status >= 400) {
        throw(new Error('Error fetching positions'))
      } else {
        return res.json()
      }
    })
}


export const getPrice = async (symbol) => {

  const url = `${urlPrefix}/prices?symbol=${symbol}`

  return await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })
    .then(res => {
      if (res.status >= 400) {
        throw(new Error('Error fetching prices'))
      } else {
        return res.json()
      }
    })
}


export const getFuturesAccountBalance = async () => {

  const url = `${urlPrefix}/futures_account_balance`

  return await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })
    .then(res => {
      if (res.status >= 400) {
        throw(new Error('Error fetching account balance.'))
      } else {
        return res.json()
      }
    })
}


export const startBot = async (requestData) => {

  const url = `${urlPrefix}/start_bot`

  const response = await fetch(url, {
    method: 'PUT',
    body: JSON.stringify(requestData),
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}


export const stopBot = async (requestData) => {

  const url = `${urlPrefix}/stop_bot`

  const response = await fetch(url, {
    method: 'PUT',
    body: JSON.stringify(requestData),
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}

export const editBot = async (requestData, pipelineId) => {

  const url = `${urlPrefix}/pipelines?pipelineId=${pipelineId}`

  const response = await fetch(url, {
    method: 'PUT',
    body: JSON.stringify(requestData),
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}

export const deleteBot = async (pipelineId) => {

  const url = `${urlPrefix}/pipelines?pipelineId=${pipelineId}`

  const response = await fetch(url, {
    method: 'DELETE',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}

export const getTradesMetrics = async (pipelineId) => {
  const url = `${urlPrefix}/trades-metrics${pipelineId ? `?pipelineId=${pipelineId}` : ''}`

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}


export const getPipelinesMetrics = async () => {
  const url = `${urlPrefix}/pipelines-metrics`

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}

export const userLogin = async (requestData) => {
  const url = `${urlPrefix}/token`

  const response = await fetch(url, {
    body: JSON.stringify(requestData),
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": getToken()
    }
  })

  return await response.json()
}

export const getEquityTimeSeries = async ({pipelineId, timeFrame}) => {

  const url = `${urlPrefix}/pipeline-equity${pipelineId ? '/' + pipelineId : ''}${timeFrame ? `?timeFrame=${timeFrame}` : ''}`

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}

export const getPipelinesPnl = async (pipelineIds) => {

  const url = `${urlPrefix}/pipelines-pnl${pipelineIds ? '/' + pipelineIds.join() : ''}`

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      "Accept": "application/json, text/plain, */*",
      "Authorization": getToken()
    }
  })

  return await response.json()
}
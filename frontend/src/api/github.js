import axios from 'axios'

export const getGithubContributions = (githubName, githubApiKey) => {
  const headers = {
    Authorization: `bearer ${githubApiKey}`,
    'Content-Type': 'application/json'
  }
  const query = `
    query {
      user(login: "${githubName}") {
        name
        contributionsCollection {
          contributionCalendar {
            colors
            totalContributions
            weeks {
              contributionDays {
                color
                contributionCount
                date
                weekday
              }
              firstDay
            }
          }
        }
      }
    }
  `
  return axios.post('https://api.github.com/graphql', { query }, { headers })
}

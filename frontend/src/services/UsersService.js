import {api, API_URL} from "./APIService";
import {PAGE_LIMIT} from "../consts";

export class UsersService {

  static fetchUsersList = (sort = null, search = null, limit = PAGE_LIMIT, offset = 0) => {
    return api.get(`${API_URL}/users/`, {params: {sort, search, limit, offset}})
  }

  static fetchUsersListByUrl = (url, sort = null, search = null) => {
    return api.get(url, {params: {sort, search}})
  }

  static createUser = (data) => {
    return api.post(`${API_URL}/users/`, data)
  }

  static deleteUser = (argyle_id) => {
    return api.delete(`${API_URL}/users/${argyle_id}`)
  }

  static fetchUserProfileData = (argyle_id) => {
    return api.get(`${API_URL}/users/${argyle_id}/profile`)
  }

  static fetchUserEmploymentsData = (argyle_id, limit = PAGE_LIMIT, offset = 0) => {
    return api.get(`${API_URL}/users/${argyle_id}/employments`, {params: {limit, offset}})
  }

  static fetchUserEmploymentsDataByUrl = (url) => {
    return api.get(url)
  }

  static fetchUserKeyMetricsData = (argyle_id) => {
    return api.get(`${API_URL}/users/${argyle_id}/key-metrics`)
  }

}


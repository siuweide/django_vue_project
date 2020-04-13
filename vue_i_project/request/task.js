import {deleteRequest, getRequest, postRequest, putRequest} from "./common";

export const getAllTasks = function () { // 获取所有的任务
    return getRequest('tasks/')
};

export const getSingleTask = function (taskId) { // 获取单个的任务
    return getRequest(`task/${taskId}`)
};

export const addTask = function (data) { // 创建任务
    return postRequest('tasks/', data)
};

export const deleteTask = function (taskId) { // 删除任务
    return deleteRequest(`task/${taskId}`)
};

export const updateTask = function (taskId, data) { // 更新任务
    return putRequest(`task/${taskId}/`, data)
};

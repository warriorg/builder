package com.warriorg.test.dao;

import java.util.List;
import com.warriorg.test.model.Predeccontainervo;

/***
 * 
 */
public interface PredeccontainervoMapper extends Mapper<Predeccontainervo> {

     /**
     * 查询获取数据
     * @param param
     * @return
     */
    List<Predeccontainervo> getList(Predeccontainervo param);

     /***
     * 批量新增
     *
     * @param list
     */
    int insertBatch(List<Predeccontainervo> list);

} 
package com.sparta.week3_s_hwk.models;

import com.sparta.week3_s_hwk.domain.Blog;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

//상속을 하자 , JPA 이용, <Blog,Long>에 확장을 할거다 - 미리 작성된 JPA소스를 들고오자
//내 생각 데이터 저장소 같은 건가?
//인터페이스는 클래스에서 멤버 변수가 없는 메서드만 있는 녀석
//BlogRepository가 extends(가져다 쓸거다) 뭐를 JpaRepository를 가져다쓸거다.
//Blog라는 클래스고 아이디는 Long인 녀석에 대해서 가져다 쓸거다
public interface BlogRepository extends JpaRepository <Blog,Long> {
    //Blog클래스에서 Blog가 테이블임을 명시하자 @Entity

    List<Blog> findAllByOrderByModifiedAtDesc();
    //findAll By OrderBy ModifiedAt Desc 수정시간된 날짜를 기준으로 내림차순으로 정렬해줘(최신순으로 정렬해줘)
    //최신순으로 정렬하는 SQL문을 JPA가 다 알아서 짜준다.
}
